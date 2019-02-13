#coding = utf-8

import json
import pprint
import re
from urllib.parse import urlencode

import requests
import lxml.html
from lxml.html import HtmlComment


def get_access_token():
    host = (
        'https://aip.baidubce.com/oauth/2.0/token?'
        'grant_type=client_credentials&client_id=enuGASLEQUNz191vAiQ1B4WA'
        '&client_secret=L0OK08w8oHZmZUhYkey45vh2vOwEHQcU'
        )
    
    headers = {
        'Content-Type' : 'application/json; charset=UTF-8'
    }
    
    result = requests.get(host, headers=headers)
    api_json_dict = json.loads(result.text)
    print(api_json_dict.get("access_token"))
    return api_json_dict.get("access_token")

def word_analyze(access_token):
    host = "https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?"
    headers = {
        'Content-Type' : 'application/json'
    }
    data = {
        "text" : "1978.3 – 1982.1 湖南大学土木工程系（工业与民用建筑专业） 工学学士"
    }
    params = {
        "charset" : "GBK",
        "access_token" : access_token,
    }
    
    full_url = host + urlencode(params)
    
    result = requests.post(full_url, headers=headers, data=json.dumps(data).encode("gbk"))
    content_dict = json.loads(result.content.decode("gbk"))
    pprint.pprint(content_dict)

def text_similar_analyze(access_token):
    host = "https://aip.baidubce.com/rpc/2.0/nlp/v2/simnet?"
    headers = {
        'Content-Type' : 'application/json'
    }
    data = {
        "text_1" : "1978.3 – 1982.1 湖南大学土木工程系（工业与民用建筑专业） 工学学士",
        "text_2" : "1982.2 – 1984.12 郑州工学院土木建筑工程系（结构工程专业） 工学硕士",
    }
    params = {
        "charset" : "GBK",
        "access_token" : access_token,
    }
    
    full_url = host + urlencode(params)
    
    result = requests.post(full_url, headers=headers, data=json.dumps(data).encode("gbk"))
    content_dict = json.loads(result.content.decode("gbk"))
    pprint.pprint(content_dict)

def email_extract(text):
    email_pattern = '^[*#\u4e00-\u9fa5 a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$'
    emails = re.findall(email_pattern, text, flags=0)
    print(emails)
    
def phone_number_extract(text):
    cellphone_pattern = '^((13[0-9])|(14[0-9])|(15[0-9])|(17[0-9])|(18[0-9]))\d{8}$'
    phoneNumbers = re.findall(cellphone_pattern, text, flags=0)
    print(phoneNumbers)
    
def structure_extract(text=None, url=None):
    if url is not None:
        response = requests.get(url)
        res_text = response.text
        html = lxml.html(res_text)
    elif text is not None:
        html = lxml.html(text)
        
    body = html.xpath("//body")
    root = body or html
    
    
    

if __name__ == "__main__":
    access_token = get_access_token()
    access_token = "24.a2e15e871163dcb5f3db21bd20f90fba.2592000.1550199092.282335-15427552"
    text_similar_analyze(access_token)



