#coding=utf-8
import os
import re
from urllib.parse import quote, urlencode

import chardet

from spider_set.spider import Spider


class WeixinSpider(Spider):
    def __init__(self, headers=None):
        
        super().__init__(headers)
    
    def get_url_list(self, 
                     url, keyword, page_start, 
                     page_end, method="GET", 
                     parmas=None):
        url_list = []
        url_pattern = re.compile('<div class="txt-box">\s*?<h3>\s*?<a.*? href\s*?=\s*?"(.*?)"')
        main_url = url
        for page in range(int(page_start), int(page_end) + 1):
            #参数编码
            method_parmas = {
                "query" : keyword,
                "page" : page,
            }
            #拼接url
            query_url = main_url + urlencode(method_parmas)
            
            if parmas:
                self.load_parmas(parmas)
            result = self.request(method, query_url)
            enc_res = chardet.detect(result.content)
            result.encoding = enc_res.get("encoding", "UTF-8")
            urls = re.findall(url_pattern, result.text)
            url_list.extend([_url.replace("amp;", "") for _url in urls])
            
        return url_list
    
    def get_url_content(self, url, nums=1):
        result = self.request(url=url)
        enc_res = chardet.detect(result.content)
        result.encoding = enc_res.get("encoding", "UTF-8")
        
        cur_dirname = os.path.dirname(__file__)
        file_store_dir = os.path.join(cur_dirname, "files")
        if not os.path.exists(file_store_dir):
            os.makedirs(file_store_dir)
        
        with open(os.path.join(file_store_dir, str(nums) + ".html"), "w+", encoding="utf-8") as f:
            f.write(result.text)
            
    def run(self):
        url = "https://weixin.sogou.com/weixin?type=2&"
        keyword = "深度学习"
        page_start, page_end = 1, 10
        url_list = self.get_url_list(url, keyword, page_start, page_end)
        
        for index, _url in enumerate(url_list, 1):
            self.get_url_content(_url, index)




if __name__ == "__main__":
    headers = {
        "Host" : "weixin.sogou.com",
        "Pragma" : "no-cache",
        "Referer" : "https://weixin.sogou.com/weixin?type=2",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "X-Requested-With" : "XMLHttpRequest",
    }
    ws = WeixinSpider(headers)
    ws.run()
    
    
        
        
        
        
        
        
        
        