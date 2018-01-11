# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask,render_template,jsonify,request,send_from_directory ,request 
import time ,json
from pymongo import MongoClient
import sys
sys.path.append('../')
from flask import make_response
from db.mysql import db_mysql
from Util.keySearch import agetfanzle
from control.mai import selctAnalysis
from flask import make_response


# from flask_cors import *

# conn =  MongoClient(host='127.0.0.1',port=27017)
# amxpage=conn['keySearch']
dbco=db_mysql()
app = Flask(__name__)

# CORS(app, supports_credentials=True)



@app.route('/#/')
def hello_world():
	return  render_template('fa.html')
 
# @app.route('/Result' ,methods=['post'])
# def Result():
# 	txt= request.form.get('txt')
# 	radio=request.form.get('radio')	
# 	cw= selctAnalysis(txt,radio)
# 	print cw
# 	return render_template('seJump/searchJump.html' , cw=cw)

# @app.route('/Add/<key>/<types>' )
# def returnKey(key,types ):
# 	print types
# 	try:
# 		if  types=='RecommendTOP' :
# 			amxpage.settopKey.insert_one({"key": key})
# 		elif types=='KeySearch':
# 			amxpage.setKey.insert_one({"key":key})	
# 		else :
# 			return  render_template('404.html')
# 		return render_template('Success.html') 
# 	except Exception as e:
# 		print e
# 		return  render_template('404.html')
# @app.route('/keywordscraper/<key>')
# def keywordscraper(key):
# 	try:

# 		return agetfanzle('http://www.fanzle.com/keywordscraper/load?q=%s&s=0&p=0&l=0&g=com'%key).get()
# 		# for keys in json.loads(cs.get())[1]:
# 		# 	if keys==key :
# 		# 		continue
# 		# 	scr={} agetfanzle('http://www.fanzle.com/keywordscraper/load?q=%s&s=0&p=0&l=0&g=com'%keys).get()

# 	except Exception as e:
# 		return 'erro'

# @app.route('/getKey/',methods=['GET'] )
# def selectKey():
# 	key,page ,allpage,lis = request.args.get('key'),0,0,[]
# 	print request.args.get('key')
# 	try:
# 		page=key.split('/')[1].split('=')[1]

# 		print  page
# 		key=key.split('/')[0]
# 		page=int(page)
# 	except Exception as e:
# 		return  render_template('404.html',)
#  	count=	amxpage.key.find({'key':key}).count()
# 	if count>0:
# 		allpage=count/50+1
# 		lis=[ obj for obj in amxpage.key.find({'key':key})]
# 	lis= lis[(page-1)*50:page*50]
# 	a=1	+((page-1)*50)
# 	for x in lis:
# 		x['a']=a
# 		a+=1
# 	print key
# 	return  render_template('index.html',lis=lis,allpage=allpage,now=page , key=key ,count=count)

# @app.route('/addKey' )
# def addKey():

# 	return  render_template('add.html')
# @app.route('/addtopKey' )
# def addtopKey():

# 	return  render_template('addKey.html')
def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun


@app.route('/articles_list/contents/')  
def json_contents():  
    response = make_response(jsonify(response=get_articles(ARTICLES_NAME)))  
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'  
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'  
    return response

def ret(txt):
	rst = make_response(txt)
	rst.headers['Access-Control-Allow-Origin'] = '*'
	return rst, 201
# @app.route('')
# def Adduers():
# 	pass




def retJson(lis ,type):
	asg=[]
	for bea in lis:
		if type=='BEA':
			asg.append({"asin":bea[0],'Rank':bea[1],'Title':bea[2],'Impressions':bea[3],'Clicks':bea[4],'Adds':bea[5],'UnitsOrdered':bea[6],'Price':bea[7],'AvgReviewRating':bea[8],'ReviewCount':bea[9],'ProductAvailableDay':bea[10],'3POffers':bea[11]})
		else:
			asg.append({'Keywords':bea[0],'Rank':bea[1],'QueryGroupCountDifference':bea[2],'Current Query Group Count':bea[3],'Previous Query Group Count':bea[4],'CurrentSearchCount':bea[5],'Previous Search Count':bea[6],'Query Group Percent Change (%)':bea[7],'Current Click Count':bea[8],'Current Add Count':bea[9],'Current Click Rate (%)':bea[10],'Current Add Rate (%)':bea[11],'Searchumb':bea[12],'SearchFbaumb':bea[13]})
	sc= str(asg).replace("{u'","{'").replace(", u'",", '")
	print sc
	return sc
def selectAsin(asin):
	sql='select *from beauty where asin="%s" ;'%(asin)
	# asg=[]
	# for bea in dbco.seclet(sql):
	# 	asg.append({'asin':bea[0],'':bea[1]})
	return ret((retJson (dbco.seclet(sql),'BEA') ))
@app.route('/selectTi/<ti>')
def selectti(ti):
	sql='select *from beauty where Title like "%s"'%('%'+ti+'%')
	return  ret(( retJson (dbco.seclet(sql),'BEA')))

@app.route('/selectkeyword/<key>')
def select(key):
	sql='select *from SearchWords where Keywords ="%s"'%(key)
	return ret( ( retJson (dbco.seclet(sql),'key')))
@app.route('/selectkeywordlike/<key>')
def selectkeywordlike(key):
	sql='select *from SearchWords where Keywords like "%s"' %('%'+key+'%')
	return  ret( (retJson (dbco.seclet(sql),"key")))

def run():
	app.run(host='0.0.0.0') 
if __name__ == '__main__':
	run()
