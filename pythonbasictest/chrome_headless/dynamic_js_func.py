#coding=utf-8
import os

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DynamicJSHandler(object):
    
    def __init__(self,**kwargs):
        
        self.driver = self.init_chrome_headless()
        
        #传入的参数
        for k,v in kwargs.items():
            setattr(self,k,v)
    
    #设置chrome headless
    def init_chrome_headless(self):
        #设置谷歌浏览器的选项
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("lang=zh_CN.UTF-8")
        #驱动的路径
        exe_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"driver","chromedriver.exe")
        #声明浏览器
        return webdriver.Chrome(executable_path=exe_path,chrome_options=chrome_options)
    
    
    def test_method(self):
        self.driver.get("https://www.baidu.com/")
        #最大化窗口
        self.driver.maximize_window()
        #获得整个访问页面
        page_source = self.driver.page_source
        #当前url
        current_url = self.driver.current_url
        #
        current_window_handle = self.driver.current_window_handle
        
        #查找元素：方法很多
        elements_a = self.driver.find_elements_by_tag_name("a")
        for a in elements_a:
            print(a.text,a.get_property("href"))
        
        #显示等待,3秒，每隔0.5秒（默认）去检测是否完成
        WebDriverWait(self.driver,3).until(EC.visibility_of(a))
        #隐式等待
        self.driver.implicitly_wait(3)
        
    #with 方式使用的实现
    def __enter__(self):
        
        return self
    
    def __exit__(self):
        
        self.driver.quit()
        
        
        
        
if __name__ == "__main__":
    handle = DynamicJSHandler()
    handle.test_method()
