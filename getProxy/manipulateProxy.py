# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests ,sys,time
sys.path.append('../')
from Util.GetConfig import GetConfig

ip=GetConfig().db_host

def get():
	try:
		ret= requests.get('http://'+ip+':5010/get/').text.replace('<br>','').replace('	','').replace(' ','').replace('\r','').replace('\n','').replace('\t','')
		return ret
	except Exception as e:
		return "error_message="+ str(e)

def delet(ip):
	 
	try:
		ret= requests.get('http://'+ip+':5010/delete/?proxy={}'.format(ip)).text.replace('<br>','').replace('	','').replace(' ','').replace('\r','').replace('\n','').replace('\t','')
		return ret
	except Exception as e:
		return "error_message="+e


if __name__ == '__main__':
	print get()