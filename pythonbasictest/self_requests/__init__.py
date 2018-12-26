import requests

'''http 请求类型'''
# r1 = requests.get('https://api.github.com/events')
# 
# r2 = requests.post('http://httpbin.org/post', data = {'key':'value'})
# 
# r3 = requests.put('http://httpbin.org/put', data = {'key':'value'})

r4 = requests.delete('http://httpbin.org/delete')
print(r4.text)

# r5 = requests.head('http://httpbin.org/get')
# 
# r6 = requests.options('http://httpbin.org/get')

'''
url参数
注意字典里值为 None 的键都不会被添加到 URL 的查询字符串里。
'''
payload = {"key1" : "value1","key2" : "value2","key3" : ['v3','v4']}
_r = requests.get("http://httpbin.org/get", params=payload)

#url
#print(_r.url)

'''
响应内容
也可以使用定制的编码
如果你创建了自己的编码，并使用 codecs 模块进行注册，
你就可以轻松地使用这个解码器名称作为 r.encoding 的值， 
然后由 Requests 来为你处理编码。
'''
#print(_r.text) #基于http头部对响应的编码做出解码

#print(_r.encoding) #响应内容的编码，可以更改

#二进制响应内容
#print(_r.content)

#以请求返回的二进制数据创建一张图片
# from PIL import Image
# from io import BytesIO
# i = Image.open(BytesIO(_r.content))

#json 响应内容
print("#-------------------#")
print(_r.json())
print("raise_for_status: ",_r.raise_for_status())
print("status_code: ",_r.status_code)

#原始响应内容
_rr = requests.get('https://api.github.com/events', stream=True)
print(_rr.raw)
print(_rr.raw.read(10))

#设置cookie
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie','yum',domain="httpbin.org",path="/cookies")
jar.set('gross_cookie','blech',domain="httpbin.org",path="/elsewhere")
url = "http://httpbin.org/cookies"
r = requests.get(url,cookies=jar)
print(r.text)
























