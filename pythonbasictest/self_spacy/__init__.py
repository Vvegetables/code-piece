#coding=utf-8
from html.parser import HTMLParser
import random
import re

import pymysql
import spacy
from spacy.tokens import Span  # 假的报错


def test1():
    nlp = spacy.load('en_core_web_sm') #英语
    doc = nlp("Hello, world. Here are two sentences.")
    
    print([t.text for t in doc])
    
    nlp_de = spacy.load('de_core_news_sm') #德语
    doc_de = nlp_de('ich bin ein berliner')
    
    print([t.text for t in doc_de])

#获取单词，名词块和句子
def test2():
    nlp = spacy.load('en_core_web_sm')
    #换行字符串写法？？？？？
    doc = nlp(u"Peach emoji is where it has always been. Peach is the superior "
              u"emoji. It's outranking eggplant 🍑 ")
    print(doc[0].text)          # Peach
    print(doc[1].text)          # emoji
    print(doc[-1].text)         # 🍑
    print(doc[17:19].text)      # outranking eggplant
    
    noun_chunks = list(doc.noun_chunks) #名词快
    print(noun_chunks[0].text)  # Peach emoji
    
    sentences = list(doc.sents) #句子
    assert len(sentences) == 3
    print(sentences[1].text)    # 'Peach is the superior emoji.'

#获取词性标签和标志
def test3():
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
    apple = doc[0]
    print('Fine-grained POS tag', apple.pos_, apple.pos) #细颗粒度的标签
    print('Coarse-grained POS tag', apple.tag_, apple.tag) #粗颗粒度的标签
    print('Word shape', apple.shape_, apple.shape) #字形
    print('Alphanumeric characters?', apple.is_alpha) #是否是字母
    print('Punctuation mark?', apple.is_punct) #是否是标点符号
    
    billion = doc[10]
    print('Digit?', billion.is_digit) #是否是数字
    print('Like a number?', billion.like_num) #意思是否像数字
    print('Like an email address?', billion.like_email) #是否像邮箱
    

#对任何字符串使用哈希值
def test4():
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(u'I love coffee')
    
    coffee_hash = nlp.vocab.strings[u'coffee']  # 3197928453018144401
    coffee_text = nlp.vocab.strings[coffee_hash]  # 'coffee'
    print(coffee_hash, coffee_text)
    print(doc[2].orth, coffee_hash)  # 3197928453018144401
    print(doc[2].text, coffee_text)  # 'coffee'
    
    beer_hash = doc.vocab.strings.add(u'beer')  # 3073001599257881079
    beer_text = doc.vocab.strings[beer_hash]  # 'beer'
    print(beer_hash, beer_text)
    
    unicorn_hash = doc.vocab.strings.add(u'🦄 ')  # 18234233413267120783
    unicorn_text = doc.vocab.strings[unicorn_hash]  # '🦄 '
    print(unicorn_hash, unicorn_text)

#识别并更新命名实体
def test5():
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(u'San Francisco considers banning sidewalk delivery robots')
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
    
    doc = nlp(u'FB is hiring a new VP of global policy')
    #手动设置实体
    doc.ents = [Span(doc, 0, 1, label=doc.vocab.strings[u'ORG'])]
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)


#训练和更新神经网络模型
def test6():
    nlp = spacy.load('en')
    train_data = [("Uber blew through $1 million", {'entities': [(0, 4, 'ORG')]})]
    
    with nlp.disable_pipes(*[pipe for pipe in nlp.pipe_names if pipe != 'ner']):
        optimizer = nlp.begin_training()
        for i in range(10):
            random.shuffle(train_data)
            for text, annotations in train_data:
                nlp.update([text], [annotations], sgd=optimizer)
    nlp.to_disk('.\model')
    
def config_db(host,username,password,dbname,port=3306):
    db = pymysql.connect(host,username,password,dbname,port)
#     db = pymysql.connect("127.0.0.1","root","","indextest")
    return db
      
    
#使用spacy的名词去实验拆分效果
def data_test():
    try:
        nlp = spacy.load('en')
        
        db = config_db("127.0.0.1","root","","indextest")
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        
        sql = " SELECT `id`,`summary`,`submission_year` FROM `australia_data`; "
        cursor.execute(sql)
        rows = cursor.fetchall()
        
        values = []
        for r in rows:
            if r["summary"]:
                doc = nlp(r["summary"])
                myset = set(map(lambda x:str(x).strip().lower(),doc.noun_chunks))
                for m in myset:
                    values.append([m,r["id"],r['submission_year']])
        
        sql = " INSERT INTO `australia_test_index`(`keyname`,`relatedid`,`year`) VALUES(%s,%s,%s); "
        cursor.executemany(sql,values)
        db.commit()
        
        sql = " SELECT `id`,`summary`,`year` FROM `australia_fellowship_data`; "
        cursor.execute(sql)
        rows = cursor.fetchall()
        
        values = []
        for r in rows:
            if r["summary"]:
                doc = nlp(r["summary"])
                myset = set(map(lambda x:str(x).strip().lower(),doc.noun_chunks))
                for m in myset:
                    values.append([m,r["id"],r['year']])
        
        sql = " INSERT INTO `australia_test_fellow_index`(`keyname`,`relatedid`,`year`) VALUES(%s,%s,%s); "
        cursor.executemany(sql,values)
        db.commit()
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    data_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    