# _*_ coding: utf-8 _*_

import ConfigParser
import io

sample_config = """
[mysqld]
user = mysql
pid-file = /var/run/mysqld/mysqld.pid
skip-external-locking
old_passwords = 1
skip-bdb
skip-innodb
"""

config_allow = ConfigParser.RawConfigParser(allow_no_value = True)
config_allow.readfp(io.BytesIO(sample_config))

print config_allow.get('mysqld', 'user')
#mysql
print config_allow.get('mysqld', 'pid-file')
#/var/run/mysqld/mysqld.pid
print config_allow.get('mysqld', 'old_passwords')
#1
print config_allow.get('mysqld', 'skip-bdb')
#None
print config_allow.get('mysqld', 'does-not-exit')
#Traceback (most recent call last):