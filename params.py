# _*_ coding: utf-8 _*_
'''
def f(*args):
	print(args, u"类型为：", type(args))

def fd(**kwargs):
	print(kwargs, u"类型为：", type(kwargs))

f()
#type tuple
fd()
#type dict
'''


tuple1 = ('selenium', 'python', 'appium')
dict1 = {'name':'james', 'age':'20', 'address':'shanghai'}

def f2(*args, **kwargs):
	return args, kwargs

print (u'参数是数值:', f2(2, 3))
#((2,3), {})
print (u'参数是列表:', f2([1, 2, 3, 4, 5, 6]))
#([1,2,3,4,5,6], {})
print (u'参数是元组:', f2(*tuple1))
#(('selenium', 'python', 'appium'), {})
print (u'参数是字典:', f2(**dict1))
#((), {'name':'james', 'age':'20', 'address':'shanghai'})

print(u'不带*元组:', f2(tuple1))
#((('selenium', 'python', 'appium'),), {})
print(u'不带**字典:', f2(dict1)){
#(({'name':'james', 'age':'20', 'address':'shanghai'},), {})