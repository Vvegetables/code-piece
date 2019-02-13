#coding=utf-8
'''
入口：
    https://weixin.sougou.com
免费代理ip：
    https://xicidaili.com
'''

import requests
from requests.sessions import Session


class Spider:
    def __init__(self, headers=None):
        self.headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        }
        
        if headers:
            self.headers.update(headers)
        
        self.session = Session()
        self.parmas = None
    
    def load_parmas(self, kwargs:dict):
        self.parmas = kwargs
    
    def request(self, method = "GET", url = None):
        if self.parmas:
            result = self.session.request(method, url, **self.parmas)
        else:
            result = self.session.request(method, url)
        
        return result
        
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.seesion.close()
        del self
        
        
        