#coding=utf-8

'''
python2的版本
'''

from functools import wraps

import MySQLdb as mysqldb

class unicode2utf8(object):
    def __init__(self, level='INFO'):
        self.level = level
         
    def __call__(self, func): # 接受函数
        @wraps(func)
        def wrapper(*args, **kwargs):
#             print "[{level}]: enter function {func}()".format(
#                 level=self.level,
#                 func=func.__name__)
            for i,a in enumerate(args,0):
                if a and isinstance(a,unicode):
                    args[i].encode('utf-8')
            for key,value in kwargs.items():
                if value and isinstance(value,unicode):
                    kwargs[key].encode('utf-8')
            func(*args, **kwargs)
        return wrapper  #返回函数

def unicode2utf8(func):
    def wrapper(*args,**kwargs):
        def tie_list(_list):
            if isinstance(_list,list):
                for i,_l in enumerate(_list,0):
                    if isinstance(_l,unicode):
                        _list[i] = _l.encode('utf-8')
                    else:
                        tie_list(_l)
            if isinstance(_list,dict):
                for key,value in _list.items():
                    if isinstance(value,unicode):
                        _list[key] = value.encode('utf-8')
                    else:
                        tie_list(_l)
            
            else:
                if isinstance(_list,unicode):
                    return _list.encode('utf-8')
                else:
                    return _list
        
        for i,a in enumerate(args,0):
            if a and isinstance(a,unicode):
                args[i].encode('utf-8')
        for key,value in kwargs.items():
            kwargs[key] = tie_list(value)
#             if value and isinstance(value,unicode):
#                 kwargs[key].encode('utf-8')
        return func(*args,**kwargs)
    return wrapper

def check_error(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            k = func(*args,**kwargs)
        except:
            return None
        return k
    return wrapper

class MysqlConnect:
    
    def __init__(self,host,username,password,dbname,port=3306):
        self.db = mysqldb.connect(host,username,password,dbname,charset='utf8',port=port)
        self.cursor = self.db.cursor(cursorclass=mysqldb.cursors.DictCursor)
        self.results = []
    
    def __del__(self):
        self.cursor.close()
        self.db.close()
        
    @unicode2utf8    
    def generate_sql(self,tablename,fields=None,values=None,_filter=None,limit=None,order_by=None,distinct=None):
        sql = []
        
        if not fields:
            fields = '*'
        else:
            if not isinstance(fields,(list)):
                raise Exception('fields 数据类型错误！应该为list')
            else:
                fields = ','.join(map(lambda x:'`'+x+'`',fields))
        if not values:
            sql.append('SELECT ')
        else:
            sql.append('INSERT INTO ')
        if distinct:
            sql.append(' DISTINCT ')
        if not values:
            sql.append(' {} FROM {} '.format(fields,tablename))
        else:
            sql.append(' {}({}) VALUES({}) '.format(tablename,fields,','.join(map(lambda x:"'".encode('utf-8') + str(x) + "'".encode('utf-8'), values))))
        
        if _filter:
            if isinstance(_filter,(str,unicode)):
                sql.append( ' WHERE {} '.format(_filter))
            else:
                raise Exception('_filter 数据类型错误！应该为str或者unicode')
        if order_by:
            if isinstance(order_by,(list)):
                sql.append(' ORDER BY {} '.format(','.join(order_by)))
            else:
                raise Exception('ORDER BY 数据类型错误！应该为list')
        if limit:
            sql.append(' LIMIT {},{}'.format(**limit))
        
        return ''.join(sql)
    
    def query(self,tablename,fields=None,_filter=None,limit=None,order_by=None,distinct=None):
        
        sql = self.generate_sql(tablename, fields=fields, _filter=_filter, limit=limit, order_by=order_by, distinct=distinct)
        self.cursor.execute(sql)
        temp = self.cursor.fetchall()
        for t in temp:
            self.results.append(t) #取出数据的时候按照t['fieldname']这种方式来。
    
    def insert(self,tablename,values,fields=None):
        try:
            sql = self.generate_sql(tablename, fields=fields, values=values)
            self.cursor.execute(sql)
            self.db.commit()
            print '成功'
        except Exception,e:
            self.db.rollback()
            print '插入失败'
    
    def batch_insert(self,tablename,values,fields=None):
        if not values:
            return 0
        sql = self.generate_sql(tablename, fields=fields, values=values[0])
        front,params = sql.split('VALUES')
        param_nums = len(params.split(','))
        sql = front + ' VALUES(' + ','.join(['%s'] * param_nums) + ') '
        n = self.cursor.executemany(sql,values)
        self.db.commit()
        return n
    
    def delete(self,tablename,_filter):
        sql = 'DELETE FROM {}'.format(tablename)
        if _filter:
            sql += ' WHERE {}'.format(_filter)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
    
    
    @check_error
    def fetch_one(self):
        if self.results:
            return self.results[0]
        else:
            return None
    
    @check_error
    def fetch_some(self,start,end):
        length = len(self.results)
        if start > length:
            start = length
        return self.results[start,end]
    
    @check_error
    def fetch_all(self):
        return self.results
    
    
    def self_exec(self,sql):
        self.cursor.execute(sql)
        temp = self.cursor.fetchall()
        for t in temp:
            self.results.append(t)
            
            
if __name__ == '__main__':
    print 'Hello'
    _connect =MysqlConnect('192.168.2.212','hanyj','Ihad#kd1234','CrawlerDB')
#     _connect.query('educationnews')
#     _connect.query('educationnews',fields=('link',))
#     print len(_connect.fetch_all())
#     _connect.insert('educationnews', fields=('title','link'), values=('测试','www.baidu.com'))
    k = _connect.batch_insert('sp_configtable', fields=['college','major','direction','method','teacher','subject'], values=[[u'003电气与控制工程学院',u'081100控制科学与工程(8)',u'01城市道路信号控制优化理论与技术(2)','全日制','刘小明(1)','①1001英语②2001控制工程基础③3001交通工程学']])
    print k
    
    
    