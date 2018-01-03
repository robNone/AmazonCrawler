# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import MySQLdb ,sys
sys.path.append('../')
from Util.GetConfig  import GetConfig
from Util.LogHandler import LogHandler
dblog=LogHandler('db',stream=False)

class db_mysql(object):
	"""docstring for db_mysql"""
	def __init__(self):
		super(db_mysql, self).__init__()
		self.config = GetConfig()

	def openCon(self):
		return  MySQLdb.connect(self.config.db_host,self.config.db_user,self.config.db_pwd,self.config.db_name) 

	def seclet(self,sql):
		db=self.openCon()
		lis=[]
		cursor = db.cursor()
		try:
			# 执行SQL语句
			cursor.execute(sql)
			# 获取所有记录列表
			results = cursor.fetchall()
			for x in results:
				lis.append(x)
		except Exception as e:
			dblog.info(e)
		finally:
			db.close()
		return lis
		
	def execute(self,sql):
		db=self.openCon()
		cursor ,ret= db.cursor(),False
		try:
			# 执行sql语句
			cursor.execute(sql)
			# 提交到数据库执行
			db.commit()
			ret= True
		except Exception as e:
			# Rollback in case there is any error
			db.rollback()
			dblog.info(e)
		# 关闭数据库连接
		finally:
			db.close()
		return ret