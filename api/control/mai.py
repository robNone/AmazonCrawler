# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import  sys,re
sys.path.append('../../')
from db.mongo  import mongodb

def  selctAnalysis(txt,type ):
	amxpage=mongodb().open()
	count=0
	if txt!=None and txt !='':
		if type=='KeySearch':
			count=amxpage.keylist.find({'key':txt}).count()
		else :
			count=amxpage.topkeylist.find({'key':txt}).count()
	else:
		txt=''
	return {'count':count ,'type':type,'txt':txt}
