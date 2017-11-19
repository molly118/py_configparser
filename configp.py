# _*_ coding: utf-8 _*_
import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('section1')
config.set('section1', 'int_a','123')
config.set('section1', 'float_b', '3.1415')
config.set('section1', 'bool_c', '1')
config.set('section1', 'baz', 'simple')
config.set('section1', 'bar', 'python')
config.set('section1', 'foo', '%(bar)s is %(baz)s!')


with open('example.cfg', 'wb') as configfile:
	config.write(configfile)