#coding=utf-8
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# print(os.path.dirname(os.path.abspath(__file__)))
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

exe_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"driver","chromedriver.exe")
print(exe_path)
 
opener = webdriver.Chrome(executable_path=exe_path,chrome_options=chrome_options)
 
opener.get("http://www.baidu.com/")
opener.find_element_by_id("kw").send_keys("selenium webdriver")
opener.find_element_by_id("su").click()
#等待3秒钟
time.sleep(3)
opener.save_screenshot("screen.png")

#关闭当前窗口 
opener.close()

#推出驱动程序
opener.quit()
