# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys ,multiprocessing
sys.path.append('../')
from Schedule.ref import runSch
from api.WebApi import run as api


def runAll():
	thread_list=[]
	pw = multiprocessing. Process(target=runSch, args=())
	pr = multiprocessing. Process(target=api, args=())
	thread_list.append(pw)
	thread_list.append(pr)
	for x in thread_list:
		x.start()

if __name__ == '__main__':
	runAll()
