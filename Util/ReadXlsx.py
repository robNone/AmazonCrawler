# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys,xlrd,re
from GetConfig import GetConfig
reload(sys) 
sys.path.append('../')
sys.setdefaultencoding('utf8')  
class FileOperation(object):
	"""docstring for read"""
	
	def __init__(self):

		super(FileOperation, self).__init__()
		con= GetConfig()
		self.filepathbea=con.fi_pathbeauty
		self.filepathkey=con.fi_pathkeywords
	def getLisKey(self ,path):
		workbook = xlrd.open_workbook(path)
		sheets = workbook.sheet_names()  
		print(str(sheets))  
		p=list()
		for i in range(len(sheets)):  
			booksheet = workbook.sheet_by_name(sheets[i])
			for row in range(booksheet.nrows):  
				row_data = []  
				for col in range(booksheet.ncols):  
					cel = booksheet.cell(row, col)  
					val = cel.value   
					row_data.append(val)  
				p.append(row_data) 
		del p[0]
		return	p
	def read(self):

		return self.getLisKey(self.filepathbea)
	def readkey(self):
		return self.getLisKey(self.filepathkey)
if __name__ == '__main__':
	
	sc=FileOperation()
	print  len(sc.read())  