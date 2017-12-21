# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pymongo import MongoClient
import sys
sys.path.append('../')
from Util.GetConfig  import GetConfig

class mongodb(object):
	"""docstring for mongodb"""
	def __init__(self,):
		super(mongodb, self).__init__()
		self.dbConfig=GetConfig()
		self.conn =  MongoClient(host=self.dbConfig.db_host,port=self.dbConfig.db_port)

	def dbcon(self):
		return self.conn[self.dbConfig.db_name]
		
	def close(self):
		self. conn.close()

if __name__ == '__main__':
	
	s=mongodb()
	print s