#coding=utf-8

'''
https://www.cnblogs.com/haigege/p/5517422.html
'''
from _stat import S_ISDIR
import os

import paramiko


class TransMachine(object):
    
    def __init__(self):
        self.linuxs = {
            "hdi_machine" : {
                "host" : "47.97.1.237",
                "port" : 22,
                "username" : "cingta",
                "password" : "KDHundsun#1",
                "dirname" : "/mnt/databack", #最后的斜杠不要添加
            },
            "ct_web_machine" : {
                "host" : "118.31.165.166",
                "port" : 22,
                "username" : "cingta",
                "password" : "kingdee#119",
                "dirname" : "/mnt/databack", #最后的斜杠不要添加
            }
        }
        self.local_store_dir = r"E:\server_data_back\sql_back" #最后的斜杠不要添加
        
        self.local_filename_handle = lambda x:list(map(lambda y:y[len(self.local_store_dir):].replace("\\","/"),x))
        self.remote_filename_handle = lambda a,b:a[len(b):]
    
    def get_all_files_in_remote_dir(self,sftp,remote_dir):
        all_files = []
        
        if remote_dir[-1] == "/":
            remote_dir = remote_dir[:-1]
            
        files = sftp.listdir_attr(remote_dir)
        for x in files:
            filename = remote_dir + "/" + x.filename
            
            if S_ISDIR(x.st_mode):  #属于linux，查看文件是否是目录
                all_files.extend(self.get_all_files_in_remote_dir(sftp, filename))
            else:
                all_files.append(filename)
        
        return all_files
    
    def get_local_filenames(self,local_dir):
        all_files = []
        files = os.listdir(local_dir)
        for f in files:
            filename = os.path.join(local_dir,f)
            
            if os.path.isdir(filename): #属于windows，查看文件是否是文件
                all_files.extend(self.get_local_filenames(filename))
            else:
                all_files.append(filename)
        
        return all_files
    
    def check_remote_file_exists(self,remote_file,local_files,remote_dir):
        short_remote_file = self.remote_filename_handle(remote_file,remote_dir)
        
        if short_remote_file in local_files:
            return True
        return False
    
    def download_files(self):
        
        short_local_filenames = self.local_filename_handle(self.get_local_filenames(self.local_store_dir))
        
        for value in self.linuxs.values():
            t = paramiko.Transport(sock=(value["host"],value["port"]))
            t.connect(username=value["username"],password=value["password"])
            sftp = paramiko.SFTPClient.from_transport(t)
            
            all_files = self.get_all_files_in_remote_dir(sftp, value['dirname'])
            
            prefix_len = len(value["dirname"])
            
            for f in all_files:
                
                if self.check_remote_file_exists(f,short_local_filenames,value['dirname']):
                    continue
                
                _f = f[prefix_len:]
                split_path = _f.split("/")
                filename,dir_name = split_path[-1],split_path[:-1]
                
                dir_name = os.path.join(*dir_name)
            
                dir_name = os.path.join(self.local_store_dir,dir_name)
                
                if not os.path.exists(dir_name):
                    os.makedirs(dir_name)
                    
                _local_path = os.path.join(dir_name,filename)
                sftp.get(f,_local_path)
            
                 
if __name__ == "__main__":
    _obj = TransMachine()
    _obj.download_files()          
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        