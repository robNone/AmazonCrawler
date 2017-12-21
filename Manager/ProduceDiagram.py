# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pymongo import MongoClient

import pymongo ,matplotlib
import matplotlib.pyplot as plt
conn =  MongoClient(host='127.0.0.1',port=27017)
amxpage=conn['keySearch']


def getList(key):
	x,y,priceList=[0,],[0,],[]
	Asinlist=amxpage.key.find({'key':key}).sort([
    ("price", pymongo.ASCENDING)])
	priceList=[num['price'] for num in Asinlist]
	counb=Asinlist.count()
	for umb in priceList:
		if y.count(umb)==0:
			x.append(priceList.count(umb))
			y.append(umb)
	# print counb
	# if (counb/50)!=0:
	# 	counb+=1
 
	# for yl in xrange (counb):
	# 	y.append(yl*50)
	# 	x.append(amxpage.key.find({"price": {"$gt": y[-2]}},{"price" :{"$lt": y[-1]}}).count())
	plt.plot(y,x)
	plt.savefig('jpg/'+key+'.png')
	# plt.seva
if __name__ == '__main__':
	print getList('assa')