#coding=utf-8
from django.core.mail import send_mail, send_mass_mail

#发送单条邮件
def send_single_email():
    #一般会在垃圾邮件中被找到
    send_mail(
        'Subject here',
        'Here is the message.', #被后面的html_message冲掉
        'hardwork_fight@163.com',
        ['625736074@qq.com'],
        fail_silently=False,
        html_message = "<h1>html_message</h1>"
    )

#发送多条邮件
def send_massive_email():
    message1 = ('Subject here', 
                'Here is the message', 
                'from@example.com', 
                ['first@example.com', 'other@example.com'])
    
    message2 = ('Another Subject', 
                'Here is another message', 
                'from@example.com', ['second@test.com'])
    
    send_mass_mail((message1, message2), fail_silently=False)
    
#给settings.ADMINS发送邮件
#mail_admins()


#给settings.MANAGERS发送邮件
#mail_managers()

def emailmessage_test():
    from django.core.mail import EmailMessage
    email = EmailMessage(
        'Hello',
        'Body goes here',
        'hardwork_fight@163.com',
        ["625736074@qq.com"],
        reply_to = ["another@example.com"],
        headers = {'Message-ID' : 'foo'}
    )










