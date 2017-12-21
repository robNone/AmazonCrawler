# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys ,time ,multiprocessing
sys.path.append('../')
from Util.keySearch import getAsinByUrl ,keTop
from pymongo import MongoClient
conn =  MongoClient(host='127.0.0.1',port=27017)
amxpage=conn['keySearch']

def  ScheduleKey():
	while True:
		one= amxpage.setKey.find_one()
		if one!=None:
			amxpage.keylist.insert({'key':one['key']})
			getAsinByUrl('https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+one['key'],one['key'])
			amxpage.setKey.delete_many(one)
		time.sleep(60)

def  ScheduleKeyotrh():
	while True:
		one= amxpage.settopKey.find_one()
		if one!=None:
			amxpage.topkeylist.insert({'key':one['key']})
			keTop('https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+one['key'],one['key'])
			amxpage.settopKey.delete_many(one)
		time.sleep(60)
def runSch():

	thread_list=[]
	pw = multiprocessing. Process(target=ScheduleKey, args=())
	pr = multiprocessing. Process(target=ScheduleKeyotrh, args=())
	thread_list.append(pw)
	thread_list.append(pr)
	for x in thread_list:
		x.start()

if __name__ == '__main__':
	runSch()