# -*- coding: utf-8 -*-
import redis
from __future__ import unicode_literals
from Util.GetConfig  import GetConfig
from Util.LogHandler import LogHandler

class Redisdb(object):
	"""docstring for Redisdb"""
	def __init__(self,):
		super(Redisdb, self).__init__()
		self.config = GetConfig()

	def function():
		pass


import redis    # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
r = redis.Redis(connection_pool=pool)
r.set('gender', 'male')     # key是"gender" value是"male" 将键值对存入redis缓存
print(r.get('gender'))

作者：君惜丶
链接：https://www.jianshu.com/p/2639549bedc8
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。