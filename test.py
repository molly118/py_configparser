# _*_ coding: utf-8 _*_

from selenimu import webdriver

d = webdriver.Chrome()

d.get('http://http://192.168.200.150:18010/exams/course-v1:TsinghuaX+JRFX01+2015_T2')

delete_name = d.execute_script("return $('#exam_list_table tr').last().children().eq(0).html()")

print delete_name