#coding=utf-8

'''
1.先安装mongodb windows 服务

2.启动运行mongodb服务器
D:\mongodb\bin\mongod --dbpath d:\data\db
'''
import datetime
import pprint

from bson.objectid import ObjectId
from pymongo import MongoClient
import pymongo


print 
#建立连接
# client = MongoClient()
# client = MongoClient('localhost',27017)
client = MongoClient('mongodb://localhost:27017')
#获得数据库
# db = client.dbname
db = client['dbname']
#获得集合
collection = db.collection_name
# collection = db['collection_name']
#文档，表现形式为json
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}
post2 = {
    "_id": 100,
    "author": "Kuber",
    "text": "This is is my first post!",
    "tags": ["Docker", "Shell", "pymongo"],
    "date": datetime.datetime.utcnow()
}
#插入文档
posts = db.posts
# post_id = posts.insert_one(post2).inserted_id
# print ('post id is ',post_id)

#获取集合
# cur_collection = db.collection_names(include_system_collections=False)
# print ('Cur_collection is',cur_collection)

#获取当个文档
pprint.pprint(posts.find_one())
# pprint.pprint(posts.find_one({'_id':ObjectId('100')}))
pprint.pprint(posts.find_one({'_id':100}))

#批量插入
new_posts = [
    {"name":'a','age':10},
    {"name":'b','age':11}
]

# results = posts.insert_many(new_posts)
# print 'results is:',results.inserted_ids

#查询多个文档
for post in posts.find():
    pprint.pprint(post)
    
#文档统计
posts.count()

#范围查询
posts.find({'date':{'$lt':datetime.datetime.now()}})

#创建索引
# result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
# print sorted(list(db.profiles.index_information()))

