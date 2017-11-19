# _*_ coding: utf-8 _*_

import ConfigParser
 
config = ConfigParser.RawConfigParser()
config.read('example.cfg')

float_b = config.getfloat('section1', 'float_b')
int_a = config.getint('section1', 'int_a')

print float_b + int_a

if config.getboolean('section1', 'bool_c'):
	print config.get('section1', 'foo')

#bool_=1  %(bar)s is %(baz)s!