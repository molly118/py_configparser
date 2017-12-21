# _*_ coding: utf-8 _*_

import requests
import json
#from requests import Cookie, Session

#r = requests.get('http://www.xuetangx.com')
#print r.headers
'''
s = requests.Session()
sg = s.get('http://www.xuetangx.com/cookies')
print(sg.text)
'''


'''
python接口cookies方法session方法有什么实际作用呢？

先初始化一个session对象，s = requests.Session() 
然后使用这个session对象来进行访问，r = s.post(url,data = user)

#import requests
reurl = r'http://www.xuetangx.com/v2/cookies'
user = {'username':'molly118','password':'molly118'}
s = requests.Session()
r = s.post(reurl,data = user) 

#print s
#requests.session.Session object at 0x02E864D0
print r.text
print r.status_code

r = requests.get('http://www.tongcheng.com')
print r.status_code
#print r.headers('Content-Type')
print r.headers.get('content-type')


#r = requests.get('https://github.com/timeline.json')
#r = requests.post('http://www.xuetangx.com/post')
#r = requests.put('http://www.xuetangx.com/put')
#r = requests.delete('http://m.ctrip.com/delete')
#r = requests.head('http://m.ctrip.com/head')

#print r.content
#print r.text


payload = {'city': u'日本', 'cityid': '2'}
r = requests.get('http://m.ctrip.com/webapp/tourvisa/visa_list', params=payload)
print r.url

payload = {'keyword': u'日本', 'salecityid': '2'}
r = requests.get('http://m.ctrip.com/webapp/tourvisa/visa_list', params=payload)
print r.url


courseorg = {'org': '3'}
r = requests.get('http://www.xuetangx.com/courses', params=courseorg)
print r.url
print r.status_code


r = requests.get('https://github.com/timeline.json')
print r.encoding
r.encoding = 'ISO-8859-1'

r = requests.get('https://github.com/timeline.json')
print r.json
#<bound method Response.json of <Response [410]>>

#定制请求头
url = 'http://m.ctrip.com'
headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecrko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
r = requests.post(url, headers=headers)
print r.request.headers
#{'Connection': 'keep-alive', 'Cookie': 'ASP.NET_SessionId=wtkwth0ovwq4rzgtbi0o1e
#tk', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'User-Agent': 'Mozilla
#/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHT
#ML, like Gecrko) Chrome/18.0.1025.166 Mobile Safari/535.19'}

url = 'http://www.xuetangx.com'
headers = {'content-type' : 'application/json'}
r = requests.post(url, headers=headers)
print r.request.headers

#{'Content-Length': '0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Us
#er-Agent': 'python-requests/2.7.0 CPython/2.7.13 Windows/8', 'Connection': 'keep
#-alive', 'content-type': 'application/json'}

url = 'http://www.xuetangx.com'
r = requests.get(url)
print r.headers

#{'content-language': 'zh-cn', 'content-encoding': 'gzip', 'transfer-encoding': '
#chunked', 'set-cookie': 'aliyungf_tc=AQAAAJ9BZCwy9Q0AN1NPdQ+2Zc2Auo1t; Path=/; H
#ttpOnly, csrftoken=RymcKPDjlwvvgqtvpYaRVPT34P7XLwTv; expires=Sat, 08-Dec-2018 11
#:20:01 GMT; Max-Age=31449600; Path=/, sessionid=67c2cf9c8cd9ff920954e1b203c6b777
#; expires=Sat, 23-Dec-2017 11:20:01 GMT; httponly; Max-Age=1209600; Path=/', 'va
#ry': 'Accept-Encoding, Accept-Encoding, Cookie, Accept-Language', 'server': 'ngi
#nx', 'connection': 'keep-alive', 'date': 'Sat, 09 Dec 2017 11:20:01 GMT', 'x-fra
#me-options': 'ALLOW', 'content-type': 'text/html; charset=utf-8'}

#复杂post请求
url = 'http://m.ctrip.com'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print r.text

#post多部分编码文件
#url = 'http://m.ctrip.com'
url = 'http://httpbin.org/post'
files = {'files': open('zxc.txt', 'rb')}
r = requests.post(url, files=files)
print r.text

url = 'http://www.xuetangx.com'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print r.request.headers
#{'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*'
#, 'user-agent': 'my-app/0.0.1'}

url = 'http://m.ctrip.com'
r = requests.get(url)
#print r.headers
#{'content-length': '26343', 'content-encoding': 'gzip', 'accept-ranges': 'bytes'
#, 'access-control-expose-headers': 'slb-http-protocol-version', 'vary': 'Accept-
#Encoding', 'server': 'Tengine/2.1.2', 'last-modified': 'Mon, 04 Dec 2017 07:12:2
#1 GMT', 'connection': 'keep-alive', 'etag': '"93c6823acf6cd31:0"', 'date': 'Mon,
# 11 Dec 2017 10:12:08 GMT', 'slb-http-protocol-version': 'HTTP/1.1', 'x-powered-
#by': 'ASP.NET', 'content-type': 'text/html'}
#print r.request.headers
#{'Connection': 'keep-alive', 'Cookie': 'ASP.NET_SessionId=5ruqz5n2mywhnkt35oqauu
#vf', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'User-Agent': 'python-
#requests/2.7.0 CPython/2.7.13 Windows/8'}
print r.headers['Content-Type']
#text/html
print r.headers.get('content-type')
#text/html

#Cookies:
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
print r.cookies['example-cookie-name']
'''
url = 'http://httpbin.org/cookies'
#url = 'http://www.xuetangx.com/cookies'
#cookies = dict(cookies_working='working')
cookies = dict(working='working', job='job')
r = requests.get(url, cookies=cookies)
#r = requests.post(url, cookies=cookies)
print r.text
#{ "cookies": {"job": "job","cookies_working": "working"}}
#print r.content
#{ "cookies": {"job": "job","cookies_working": "working"}}

