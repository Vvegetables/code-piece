#coding=utf-8

'''
官方文档地址：http://docs.sqlalchemy.org/en/latest/orm/index.html
'''

from sqlalchemy import engine
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.session import sessionmaker

#建立模型需要的基类
Base = declarative_base()

#method1
def get_session_1():
    config = {
        "username" : "",
        "password" : "",
        "host" : "",
        "port" : 3306,
        "dbname" : ""
    }

    engine = create_engine('mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}'.format(**config))
    
    Session = sessionmaker(bind=engine)

#method2
def get_session_2():
    # configure Session class with desired options
    Session = sessionmaker()
    
    # later, we create the engine
    engine = create_engine('postgresql://...')
    
    # associate it with our custom Session class
    Session.configure(bind=engine)
    
    # work with the session
    session = Session()
    
    
    
    

