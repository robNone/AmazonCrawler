# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# !/usr/bin/env python

import os
from utilClass import ConfigParse
from utilClass import LazyProperty


class GetConfig(object):
    """
    to get config from config.ini
    """

    def __init__(self):
        self.pwd = os.path.split(os.path.realpath(__file__))[0]
        self.config_path = os.path.join(os.path.split(self.pwd)[0], 'Config.ini')
        self.config_file = ConfigParse()
        self.config_file.read(self.config_path)
        print self.config_file

    @LazyProperty
    def db_type(self):
        return self.config_file.get('DB', 'type')
    @LazyProperty
    def  Redisdb_host(self):
        return self.config_file.get('Redisdb', 'host')
    @LazyProperty
    def  Redisdb_port(self):
        return self.config_file.get('Redisdb', 'port')
    @LazyProperty
    def  Redisdb_dbname(self):
        return self.config_file.get('Redisdb', 'dbname')
    @LazyProperty
    def db_name(self):
        return self.config_file.get('DB', 'name')

    @LazyProperty
    def db_host(self):
        return self.config_file.get('DB', 'host')

    @LazyProperty
    def db_user(self):
        return self.config_file.get('DB', 'user')
    @LazyProperty
    def db_pwd(self):
        return self.config_file.get('DB', 'pwd')
    @LazyProperty
    def fi_path(self):
        return self.config_file.get('FilePath', 'path')

    @LazyProperty
    def db_port(self):
        return int(self.config_file.get('DB', 'port'))

    @LazyProperty
    def proxy_getter_functions(self):
        return self.config_file.options('ProxyGetter')

    @LazyProperty 
    def host_ip(self):
        return self.config_file.get('HOST','ip')

    @LazyProperty
    def host_port(self):
        return self.config_file.get('HOST', 'port')

if __name__ == '__main__':
    gg = GetConfig()
    print(gg.Redisdb_dbname)
    print(gg.db_name)
    print(gg.db_host)
    print(gg.db_port)
    print(gg.db_pwd)
    print(gg.host_ip)
    print(gg.path)
