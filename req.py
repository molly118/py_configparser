# _*_ coding: utf-8 _*_

import requests
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
'''
r = requests.get('http://www.tongcheng.com')
print r.status_code
#print r.headers('Content-Type')
print r.headers.get('content-type')