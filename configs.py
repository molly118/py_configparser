# _*_ coding: utf-8 _*_

import ConfigParser

configs = ConfigParser.SafeConfigParser({'bar': 'life', 'baz': 'hard'})
config_exam = 'example.cfg'
#configs.read('example.cfg')
configs.read(config_exam)

print configs.get('section1', 'foo')
#pyton is simple!
configs.remove_option('section1', 'bar')
configs.remove_option('section1', 'baz')
print configs.get('section1', 'foo')
#life is hard!
