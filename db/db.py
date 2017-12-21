# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pymongo import MongoClient



conn =  MongoClient(host='127.0.0.1',port=27017)
amxpage=conn['keySearch']


def getList(key):
	Asinlist=amxpage.key.find({'key':key})

	if (Asinlist.count/50!)=0:
		pass

	for x in Asinlist.count:
		pass