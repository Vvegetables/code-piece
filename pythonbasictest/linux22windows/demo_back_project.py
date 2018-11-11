#coding=utf-8
from _stat import S_ISDIR
import datetime
import json
import os

import paramiko

try:
    import cPickle as pickle
except:
    import pickle


class BackProject:
    
    def __init__(self):
        self.linuxs = self.load_local_config(os.path.join(os.path.dirname(__file__),"download_addr.txt"))
#         self.linuxs = {
#             "hdi_machine" : {
#                 "host" : "47.97.1.237",
#                 "port" : 22,
#                 "username" : "cingta",
#                 "password" : "KDHundsun#1",
#                 "dirname" : "/mnt/databack", #最后的斜杠不要添加
#             },
#             "ct_web_machine" : {
#                 "host" : "118.31.165.166",
#                 "port" : 22,
#                 "username" : "cingta",
#                 "password" : "kingdee#119",
#                 "dirname" : "/mnt/databack", #最后的斜杠不要添加
#             }
#         }
        # self.download_addr = r'E:\server_data_back\program\download_addr.txt'
        self.local_store_dir = r"E:\server_data_back\data_back" #最后的斜杠不要添加
        
#         self.local_filename_handle = lambda x:list(map(lambda y:y[len(self.local_store_dir):].replace("\\","/"),x))
#         self.remote_filename_handle = lambda a,b:a[len(b):]
        
        self.local_record = self.load_local_config(os.path.join(os.path.dirname(__file__),"local_record.txt"))
    
    def load_local_config(self,filename):
        receiver = []
        if "download" in filename:
            with open(filename,'r',encoding="utf-8") as f:
                for chunk in f:
                    receiver.append(chunk)
                receiver = "".join(receiver)
                if not receiver:
                    return {}
                
                return eval(receiver)

        else:
            with open(filename,'rb') as f:
                try:
                    return pickle.load(f)
                except EOFError:
                    return {}
        
    def get_all_files_in_remote_dir(self,sftp,remote_dir):
        all_files = []
        
        if remote_dir[-1] == "/":
            remote_dir = remote_dir[:-1]
        
        try:    
            files = sftp.listdir_attr(remote_dir)
        except UnicodeDecodeError:
            print(remote_dir)
            with open("back_err.txt",'a+',encoding="utf-8") as f:
                f.write(json.dumps({"err_file":remote_dir,"datetime":datetime.datetime.now().strftime("%y-%m-%d %H:%I:%S"),"reason":"UnicodeDecodeError"}))
            return []
        
        for x in files:
            filename = remote_dir + "/" + x.filename
            
            if S_ISDIR(x.st_mode):  #属于linux，查看文件是否是目录
                all_files.extend(self.get_all_files_in_remote_dir(sftp, filename))
            else:
                if (filename not in self.local_record) or (filename in self.local_record and x.st_mtime != int(self.local_record.get(filename))): #根据修改事件过滤过滤
                    all_files.append(filename)
                    self.local_record[filename] = x.st_mtime
        
#         with open(os.path.join(os.path.dirname(__file__),"local_record.txt"),"wb") as f:
#             pickle.dump(self.local_record,f)
                    
        return all_files
    
#     def check_remote_file_exists(self,remote_file,local_files,remote_dir):
#         short_remote_file = self.remote_filename_handle(remote_file,remote_dir)
#         
#         if short_remote_file in local_files:
#             return True
#         return False
    
    def download_files(self):
        
        for value in self.linuxs.values():
            t = paramiko.Transport(sock=(value["host"],int(value["port"])))
            t.connect(username=value["username"],password=value["password"])
            sftp = paramiko.SFTPClient.from_transport(t)
            
            all_files = self.get_all_files_in_remote_dir(sftp, value['dirname'])
    
            prefix_len = len(value["dirname"])
            
            for f in all_files:
                _f = f[prefix_len:]
                split_path = _f.split("/")
                filename,dir_name = split_path[-1],split_path[:-1]
                
                dir_name = os.path.join(*dir_name)
            
                dir_name = os.path.join(self.local_store_dir,dir_name)
                
                if not os.path.exists(dir_name):
                    os.makedirs(dir_name)
                    
                _local_path = os.path.join(dir_name,filename)
                try:
                    sftp.get(f,_local_path)
                except FileNotFoundError:
                    print(filename,f)
                    with open("back_err.txt",'a+',encoding="utf-8") as f:
                        f.write(json.dumps({"err_file":f,"datetime":datetime.datetime.now().strftime("%y-%m-%d %H:%I:%S"),"reason":"FileNotFoundError"}))
                except OSError:
                    print(filename,f)
                    with open("back_err.txt",'a+',encoding="utf-8") as f:
                        f.write(json.dumps({"err_file":f,"datetime":datetime.datetime.now().strftime("%y-%m-%d %H:%I:%S"),"reason":"OSError"}))
            with open(os.path.join(os.path.dirname(__file__),"local_record.txt"),"wb") as f:
                pickle.dump(self.local_record,f)
                
if __name__ == "__main__":
#     print(os.path.dirname(__file__))
    _obj = BackProject()
    _obj.download_files()
    
    
    
    
    
    
    