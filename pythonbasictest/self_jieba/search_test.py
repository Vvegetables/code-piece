#coding=utf-8
import jieba
import pymysql
from collections import namedtuple
# pymysql.install_as_MySQLdb()

class SearchTest:
    '''
    '''
#     class DBInfos:
#         def __init__(self,ids=[],appearnums=0):
# #             self.key = key
#             self.ids = ids
#             self.appearnums = appearnums
    
    def __init__(self,tablename):
        self.tablename = tablename
#         self.table_fields = table_fields
        self.host = "127.0.0.1"
        self.dbname = "indextest"
        self.user = "root"
        self.password = ""
        self.port = 3306
        self.db = None
        self.store_dict = {}
    
    def generate_cloud_words(self):
        pass
        
        
    def connect(self):
        self.db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.dbname,port=self.port)
    
    def config_mysql(self,host,username,password,dbname,port):
        self.host = host
        self.username = username
        self.password = password
        self.dbname = dbname
        self.port = port
        
        self.db = self.connect()
        
    def participle_words(self):
        if not self.db:
            raise Exception("先config_mysql")
        
#         DBInfos = namedtuple("DBInfos",["ids","appearnums"])
#         defaultdict(DBInfos)
        
        
        _cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        
        sql_query = "select id,projectname,year from t_rp_nationalnaturalscifund"
        
        _cursor.execute(sql_query)
        
        results = _cursor.fetchall()
        try:
            for i,row in enumerate(results,1):
                _id = row["id"]
                projectname = row["projectname"]
                year = row['year']
                
                seg_list = jieba.cut_for_search(projectname) #搜索引擎模式
                
                for seg in seg_list:
                    if seg in self.store_dict:
                        self.store_dict[seg].append((_id,year))
                    else:
                        self.store_dict[seg] = [(_id,year)]
        except Exception as e:
            print(i,e)
        
        return self.store_dict

    def create_table(self,tablename):
        create_sql = '''
        	DROP TABLE IF EXISTS {};'''.format(tablename) + '''
            CREATE TABLE '''+tablename+'''(
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                keyname VARCHAR(500) NOT NULL,
                relatedid TEXT NOT NULL,
                year INT NOT NULL
            );
        '''
        
        _cursor = self.db.cursor()
        try:
            _cursor.execute(create_sql)
        except:
            pass
        
        sql_data = []
        
        if self.store_dict:
            for key,value in self.store_dict.items():
#                 value[0] = ",".join(map(lambda x:str(x),value[0]))
                for v in value:
                    sql_data.append([key,v[0],v[1]])
            
        try:
            print("准备插入数据...")
            _cursor.executemany("INSERT INTO " + tablename + "(keyname,relatedid,year) VALUES(%s,%s,%s)",sql_data)
            print("开始插入数据...")
            self.db.commit()  
            print("完成数据插入。")
        except Exception as e:
            print(e)
        finally:
            _cursor.close()
            self.db.close()
        
            
if __name__ == "__main__":
    _obj = SearchTest("t_rp_nationalnaturalscifund")   
    _obj.connect()
    _obj.participle_words()  
    _obj.create_table("one_line_fenci")
        
            
    
    
    
    
    
    
    
    