# _*_ coding: utf-8 _*_

import ConfigParser

configc = ConfigParser.ConfigParser()
configc.read('example.cfg')

print configc.get('section1', 'foo', 0)
#python is simple
print configc.get('section1', 'foo', 1)
#%(bar)s is %(baz)s!
print configc.get('section1', 'foo', 0, {'baz': 'are', 'bar': 'am'})
#am is are