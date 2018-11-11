#coding=utf-8

'''
https://www.cnblogs.com/pizitai/p/6398632.html
paramik 是一个强大的ssh连接模块。
'''

import datetime
import os

import paramiko

from linux22windows.config import param


hostname = param.get("host")
username = param.get("username")
port = param.get("port")
password = param.get("password")

def upload(local_dir,remote_dir):  
    try:  
        t=paramiko.Transport((hostname,port))  
        t.connect(username=username,password=password)  
        sftp=paramiko.SFTPClient.from_transport(t)  
        print('upload file start %s ' % datetime.datetime.now())  
        for root,dirs,files in os.walk(local_dir):  
            print('[%s][%s][%s]' % (root,dirs,files))  
            for filespath in files:  
                local_file = os.path.join(root,filespath)  
                print(11,'[%s][%s][%s][%s]' % (root,filespath,local_file,local_dir))  
                a = local_file.replace(local_dir,'').replace('\\','/').lstrip('/')  
                print('01',a,'[%s]' % remote_dir)  
#                 remote_file = os.path.join(remote_dir,a)  
                remote_file = remote_dir + "/" + a
                print(22,remote_file)  
                try:  
                    sftp.put(local_file,remote_file)  
                except Exception as e:  
                    sftp.mkdir(os.path.split(remote_file)[0])  
                    sftp.put(local_file,remote_file)  
                    print("66 upload %s to remote %s" % (local_file,remote_file))  
            for name in dirs:  
                local_path = os.path.join(root,name)  
                print(0,local_path,local_dir)  
                a = local_path.replace(local_dir,'').replace('\\','')  
                print(1,a)  
                print(1,remote_dir)  
                remote_path = os.path.join(remote_dir,a)  
                print(33,remote_path)  
                try:  
                    sftp.mkdir(remote_path)  
                    print(44,"mkdir path %s" % remote_path)  
                except Exception as e:  
                    print(55,e)  
        print('77,upload file success %s ' % datetime.datetime.now())  
        t.close()  
    except Exception as e:  
        print(88,e) 
        
        
def remote_scp(host_ip,remote_path,local_path,username,password):  
    t = paramiko.Transport((host_ip,22))  
    t.connect(username=username, password=password)  
    sftp = paramiko.SFTPClient.from_transport(t)  
    src = remote_path  
    des = local_path  
    sftp.get(src,des)  
    t.close() 
    
    
if __name__ == "__main__":
#     local_dir=r'C:\Users\Zcxu\Desktop\conf.d'  
#     remote_dir='/mnt/cingtahdi/hdiback/static/img'  
#     upload(local_dir,remote_dir)  
    
    
    remote_path = '/mnt/cingtahdi/hdiback/static/img/pw_full.png'  
    local_path = r'E:\test\pw_full.png'
     
    remote_scp(hostname,remote_path,local_path,username,password)   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         