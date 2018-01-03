# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys ,hashlib
sys.path.append('../')
from db.mysql import db_mysql


class RegisterOrLogin(object):
	"""docstring for ClassName"""
	def __init__(self, name,pwd,email=None):
		super(RegisterOrLogin, self).__init__()
		self.name = name
		self.pwd   = pwd
		self.email = email
		self.db     = db_mysql()
	def getInsertSql(self):
		return "INSERT INTO user	VALUES  (0,'%s','%s',%s)"%(self.name,self.pwd,self.email)
	def getSelectSql(self)
		return "SELECT  id FROM  user WHERE  name ='%s' and pwd ='%s'"%(self.name,self.pwd)
	def insert(self):
		sql=self.getInsertSql()
		return self.db.execute(sql)
	def  slectUser(self):
		sql=self.getSelectSql()
		return self.db.seclet(sql)

class setSession(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(setSession, self).__init__()
		self.arg = arg
		