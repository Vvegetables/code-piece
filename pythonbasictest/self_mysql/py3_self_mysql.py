#coding=utf-8
from functools import wraps

import pymysql as mysqldb

#捕获错误的装饰器
def check_error(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            k = func(*args,**kwargs)
        except Exception as e:
            print(e)
            return None
        return k
    return wrapper

class SelfPymysql:
    def __init__(self,host,username,password,dbname,port=3306):
        #charset字段不能放
        self.db = mysqldb.connect(host,username,password,dbname,port=port)
        #键值对的形式返回查询结果
        self.cursor = self.db.cursor(cursor=mysqldb.cursors.DictCursor)
        self.results = []
    
#     def __del__(self):
#         self.cursor.close()
#         self.db.close()
    
    '''
    判断一个对象是否可迭代：
    isinstance(obj,Iterable)
    '''
    #生成sql脚本：select and insert    
    def generate_sql(self,tablename:str,fields:list=None,values:list=None,_filter=None,limit=None,order_by=None,distinct=None) -> str:
        sql = []
        #格式化取出的参数
        if not fields:
            fields = "*"
        else:
            if not isinstance(fields,list):
                raise Exception("fields 数据类型错误！应该是list")
            else:
                fields = ','.join(map(lambda x:'`'+x+'`',fields))
        #根据是否有values这个参数判断是select操作还是insert操作
        if not values:
            sql.append('SELECT ')
        else:
            sql.append('INSERT INTO ')
        
        #查看是否有distinct这个参数
        if distinct:    
            sql.append(' DISTINCT ')
        
        #查看是否有values这个参数，进行select 和 insert操作的转变
        if not values:
            sql.append(' {} FROM {} '.format(fields,tablename))
        else:
            sql.append(' {}({}) VALUES({}) '.format(tablename,fields,','.join(map(lambda x:"'" + str(x) + "'", values))))
        
        if _filter:
            if isinstance(_filter,str):
                sql.append( ' WHERE {} '.format(_filter))
            else:
                raise Exception('_filter 数据类型错误！应该为str') 
            
        if order_by:
            if isinstance(order_by,list):
                sql.append(' ORDER BY {}'.format(','.join(order_by)))
            else:
                raise Exception('ORDER BY 数据类型错误！应该为list')
        
        if limit:
            sql.append(' LIMIT {},{}'.format(**limit))
        
        return ''.join(sql)
    
    #执行查询语句
    def query(self,tablename,fields=None,_filter=None,limit=None,order_by=None,distinct=None):
        sql = self.generate_sql(tablename, fields=fields, _filter=_filter, limit=limit, order_by=order_by, distinct=distinct) 
        self.cursor.execute(sql)
        temp = self.cursor.fetchall()    
        self.results = []
        for t in temp:
            self.results.append(t) #取出数据的时候按照t['fieldname']这种方式来。    
        
    #执行插入语句    
    def insert(self,tablename,values,fields=None):
        try:
            sql = self.generate_sql(tablename, fields=fields, values=values)
            self.cursor.execute(sql)
            self.db.commit()
            print('插入成功')
        except Exception as e:
            self.db.rollback()
            print('插入失败',e)        
    
    #执行批量插入语句        
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
    
    #执行删除语句
    def delete(self,tablename,_filter):
        sql = 'DELETE FROM {}'.format(tablename)
        if _filter:
            sql += ' WHERE {}'.format(_filter)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()  
    
    #获取第一条数据        
    @check_error
    def fetch_first(self):
        if self.results:
            return self.results[0]
        else:
            return None 
    
    #获取区间内的数据    
    @check_error
    def fetch_some(self,start,end):
        length = len(self.results)
        if start > length:
            start = length
        return self.results[start:end]
    
    #获取所有数据
    @check_error
    def fetch_all(self):
        return self.results
    
    #执行sql脚本
    def self_exec(self,sql):
        self.cursor.execute(sql)
        self.results = self.cursor.fetchall()
#         self.results = []
#         for t in temp:
#             self.results.append(t)     
  
  
if __name__ == '__main__':
    
    _connect = SelfPymysql('47.96.253.99','ct','IhadKD#4321','innerweb')
#     _connect.query('sp_configtable')
    _connect.query('sp_configtable',fields=['link'])
    print(_connect.fetch_some(0, 2))
#     print(_connect.results)
#     print(len(_connect.fetch_all()))
#     _connect.insert('educationnews', fields=('title','link'), values=('测试','www.baidu.com'))
#     k = _connect.batch_insert('sp_configtable', fields=['title','subtitle','link','type','visited','number'], values=[[]])
#     print(k)      