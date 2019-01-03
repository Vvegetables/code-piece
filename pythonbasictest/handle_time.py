#coding=utf-8
from datetime import datetime, timedelta
import time


class time_util:
    
    def time_cal(self):
        #timedelta(days,seconds,microseconds,milliseconds,minutes,hours,weeks)
        _now = datetime.today()
        #datetime可以直接进行运算和比较
        print 'datetime.today:',datetime.today()
        print 'datetime.now:',datetime.now()
        print 'datetime.now().strftime("%Y-%m-%d-%H-%M-%S"):',datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        print 'datetime.now().year:',datetime.now().year
        
        #replace()方法允许我们对datetime的任意字段进行替换，并返回一个新的datetime对象，这个新的对象在其他字段上与原有对象保持一致。
        print 'datetime.now().replace(month=10):',_now.replace(month=10)
        
        #datetime.timetuple功能十分强大！跟namedtuple很相似
        t = datetime.now().timetuple()
        print 'datetime.now().timetuple()的读取：',len(t),t[0],t.tm_hour,t
        
        print 'time.time():',time.time()
        print 'time.gmtime(time.time()):',time.gmtime(time.time()) #将时间戳转换成标准time格式的时间的timetuple，也就是有时差
        print 'time.mktime(time.time()):',time.mktime(time.gmtime(time.time())) #将timetuple转换成时间戳
        print 'time.localtime():',time.localtime()
        
    
    def time_transfer(self):
        _now = datetime.now()
        
    def timestamp_transfer(self,param):
        #datetime转换成时间戳
        if isinstance(param,datetime):
            print time.mktime(param)
        
        #时间戳转换成需要的格式,方式一转成time
        if isinstance(param,(float)):
            print '方式一：time.localtime(float) =',time.localtime(param)
        #方式二转成datetime
        if isinstance(param,(float)):
            print '方式二：datetime.utcfromtimestamp(float) =',datetime.utcfromtimestamp(param) #这个是标准时间，比如这个时间就和中国的北京时间相差8个小时，如果你是在中国，那么需要个这个转换的datetime加上8个小时。
            print '方式二：datetime.fromtimestamp(float) =',datetime.fromtimestamp(param) #等于当地时间
if __name__ == '__main__':
    time_util().time_cal()
    print '=' * 30
    time_util().timestamp_transfer(1381419600.00)
    print '=' * 30
    time_util().time_transfer()
    
    
    
    
    
    
    
    
    
    
    