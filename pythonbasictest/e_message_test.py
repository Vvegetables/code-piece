#coding=utf-8
import json


try:
    9 / 0
except Exception as e:
    print (e)
    print (json.dumps({'data':str(e)}))