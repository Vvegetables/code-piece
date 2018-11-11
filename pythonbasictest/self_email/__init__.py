#coding=utf-8

'''
SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,
它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。
'''

from email.mime.text import MIMEText
import smtplib
from email.header import Header

#第三方 SMTP服务
mail_host="smtp.sina.com"  #设置服务器
# mail_user="17826852205@sina.cn"    #用户名
# mail_pass="7758258ZCX"   #口令 

#发送者
sender = '17826852205@sina.cn'
#接收者
receivers = '625736074@qq.com'

#设置邮件内容
message = MIMEText('你好，欢迎加入我们这个大家庭！',"plain","utf-8")

message["From"] = Header(sender)
message["To"] = Header('赵崇旭'+'<'+receivers+'>',"utf-8")

#主题
subject = "邮件发送"
message["Subject"] = subject

try:
    #如果我们本机没有 sendmail 访问，也可以使用其他邮件服务商的 SMTP 访问（QQ、网易、Google等）。
#     smtpObj = smtplib.SMTP("localhost")
    #第三方服务
    smtpObj = smtplib.SMTP(mail_host)
#     smtpObj.connect(mail_host, 25)
#     smtpObj.set_debuglevel(1)
    smtpObj.login(sender,"123qweasdzxc")
    #发送
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("发送成功")
except Exception as err:
    print(err)