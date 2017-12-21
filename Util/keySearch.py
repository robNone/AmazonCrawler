# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re,multiprocessing.process  ,Spider ,time ,threading,sys
from lxml import etree
from  multiprocessing import  process
from pymongo import MongoClient
from LogHandler import LogHandler
sys.path.append('../')
reload(sys)
sys.setdefaultencoding('utf8')  
import time
headers ={ 
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
	        "Host":"www.amazon.com",
	    	"Accept-Language":"zh-CN,zh;q=0.8",
"Cookie":	'aws-target-static-id=1497838335626-19381; s_vn=1529374335856%26vn%3D1; regStatus=pre-register; aws_lang=cn; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1497838335629-9703.24_4; amznacsleftnav-1e4dfe77-0d78-3527-b54a-f23cc2cb231e=1; AMCVS_4A8581745834114C0A495E2B%40AdobeOrg=1; AMCV_4A8581745834114C0A495E2B%40AdobeOrg=-894706358%7CMCIDTS%7C17415%7CMCMID%7C15071633912452894915662900002460765377%7CMCOPTOUT-1504585615s%7CNONE%7CMCAID%7C2CD68D00852A8569-40000301C00003C7%7CvVersion%7C2.3.0; s_lv=1504578420898; appstore-devportal-locale=zh_CN; s_vnum=1931133517751%26vn%3D4; s_nr=1504749318700-Repeat; s_dslv=1504749318701; s_ppv=85; at-main=Atza|IwEBIDDWvxoMHsifLiTWazK1cSAb6sPs44jFlHu4oL3LodNKVsU8NGdSm5K8FdmMWr__wQDtiusZ88pZrsaXKPN42AIgcztHnSaeYEUHhgy0P3sil04wpCLe2F1m_HK7eZDg0D6bxXBzGOttA8lN4Um0cObimx2j07DNb1KHtgA465FpjPDMqWfHdw_Uvy4vKwfqIzwSp2nO3iqK1VlRDQlcNCHFi33PfESso3Up1yHvkhiqBlVSVl-GSm7a49vnTMX-xGIhPWqDBCSEunEF8nPTZ1Y4zM0RCnQojWjaCiesNq_3iy3PgL-LKEEmxTNe6RixwK3d2Swd8dWjcy743XEdxa4xUeiD9wtrT8Zx0hyWIYejSDm7W0REBeViHrYNw8Pr927I5Vrlm6rN23psIff2--yF; sess-at-main="goK1tVYcgb7R2XcYasQ8/+2ABnZO2hdIYIDDrbHkOiM="; x-wl-uid=1XXT7ohIeJZyY/7sC/ytnTHT+Vwn62xt/Jqr4l2xe+WetZvII2HlOUcCgEXfKRBNwgbOTZrrdaMcZJNwjXVH48GrQ2/ROuA6CLbVJ1xZ9Jo0PgAxPQ9L1NbmGgdG1oBrv+QyImd7kzKk=; skin=noskin; JSESSIONID=5AF6FA51D68211D42C8B1E4F272968D3; s_sess=%20s_ppvl%3D%3B%20s_ppv%3DUS%25253AAZ%25253ASOA-overview-seeall%252C92%252C37%252C3448%252C2880%252C1348%252C1920%252C1080%252C0.67%252CL%3B%20s_cc%3Dtrue%3B%20c_m%3DundefinedTyped/BookmarkedTyped/Bookmarked%3B%20s_sq%3Dacsus-prod%253D%252526pid%25253D508510%252526pidt%25253D1%252526oid%25253Dhttps%2525253A%2525252F%2525252Fwww.amazon.com%2525252Fgp%2525252Fhelp%2525252Fcustomer%2525252Fforums%2525252Fkindleqna%2525252Fref%2525253Dhp_gt_comp_ss_forum_Kindle%252526ot%25253DA%3B; s_pers=%20s_fid%3D0B584A252E26D24B-0508DABA67938BE2%7C1662514482807%3B%20s_dl%3D1%7C1507518928552%3B%20gpv_page%3DUS%253ASC%253A%2520SellerCentralLogin%7C1507518928555%3B%20s_ev15%3D%255B%255B%2527Typed/Bookmarked%2527%252C%25271507517128514%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271507517128557%2527%255D%255D%7C1665283528557%3B; x-main="Ihat36AUznBqU@bAXSLMRPKxSgCxnH1bEUQiqvtsIVRnH75aplq29jnQqj?LHESj"; lc-main=en_US; session-token="STQf3qhsr7tRS9RXdV+B5iLxVuHXTWxw3sz5jRhYxXQ8OePnWMVSkTiU5Wot7+yBX2/sYgnK2b585EUmLISbef7iNSg9mAtKSxMrAgH3WlNomIsvZw5cciATBtgld6xxTLN0L4qRqPXGW6ucpWuX9M0yI4EWddIswJKbCJK56B27pyn72QR0wPvzVVODwGZRxTxjBywnAJfXhbq/zyaIytgH0BvgASM5FAp6FyMVO7E/dq31m2t0EQY1Jx+jmFu6/mZy03RzzDPWKOZKlpVMSg=="; ubid-main=131-0601013-2724535; session-id-time=2082787201l; session-id=136-1823294-1208816; csm-hit=TC76C8PW39N5MY6AKGWM+s-FTFB6ESPHJ74V4N2XPGW|1507777709001'

            }

csheaders ={ 
			"Accept":"application/json, text/javascript, */*; q=0.01",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
	        "Host":"www.fanzle.com",
	    	"Accept-Encoding":"gzip, deflate",
	    	"Accept-Language":"zh-CN,zh;q=0.9",
	    	"X-Requested-With":"XMLHttpRequest"
            }

keylog=LogHandler('keylog')
toplog=LogHandler('toplog')
keylog=LogHandler('key')
conn =  MongoClient(host='127.0.0.1',port=27017)
amxpage=conn['keySearch']

class getPage(object):
	"""docstring for getPage"""
	def __init__(self, url):
		super(getPage, self).__init__()
		self.url = url
		
	def generateData(self):
		return {'url':self. url,'headers':headers,'timeout':3,'ac':None}

	def get(self):
		return Spider.request(self.generateData()).doerro()

class agetfanzle(getPage):
	"""docstring for ClassName"""
	def generateData(self):
		return {'url':self. url,'headers':csheaders,'timeout':3,'ac':True}
		
def getAsinByUrl(url,key):
	sqn=getPage(url).get()
	while True:
		#amxpage.a.insert({'url':url,"sqn":sqn})
		# multiprocessing.Process(target = findAsin, args = (asin,key,))
		findAsin(sqn,key)
		if sqn.find('lastPageRightArrow')>0:
			print url+'end'
			break
		try:
			if sqn.find('a-carousel-viewport')<0:
				url=sqn[sqn.find('id="pagnNextLink"'):].split('"')[5].replace('amp;','')
			sqn=getPage(url).get()

			

		except Exception as e:
	 		f=file( 'sas.txt',"w+")
			f.writelines(sqn)
			f.close()
			continue




def findAsin(page,key):

	li=re.split(r'data-asin=',page)  

	del li[0]
	thread_list = [] 
	for x in li:
		if amxpage.asins.find_one(({"asin":x.split('"')[1]}))!=None:
			continue
		amxpage.asins.insert_one({'asin':x.split('"')[1]})
		t =threading.Thread(target=getpageByason,args=(x.split('"')[1],key,))
		print x.split('"')[1]
		thread_list.append(t)	
	for t in thread_list:
		t.start()
	# for t in thread_list:
	# 	t.join()
			# f=file( 'dest.txt',"a+")
			# f.writelines('   '+x.split('"')[2])
			# f.close()
def getTitle(asin):
	page=getPage('https://www.amazon.com/dp/'+asin).get()
	return page[page.find('id="productTitle"'):].split('>')[1].split('<')[0].strip()
def sctr(str):
	return re.split('a-size-base a-spacing-small a-spacing-top-small a-text-normal',str)[1]
def getTcumb(keywords):
	sf='https://www.amazon.com/mn/search/ajax/gp/search/ref=sr_nr_p_85_0?fst=as%3Aoff&rh=i%3Aaps%2Ck%3Astnb&keywords=stnb&ie=UTF8&qid=1513606844&fromHash=%2Fgp%2Fsearch%2Fref%3Dsr_nr_p_85_0%3Ffst%3Das%253Aoff%26rh%3Di%253Aaps%252Ck%253Astnb%252Cp_85%253A2470955011%26keywords%3Dstnb%26ie%3DUTF8%26qid%3D1513606478%26rnid%3D2470954011&section=ATF,BTF&fromApp=gp%2Fsearch&fromPage=results&fromPageConstruction=auisearch&version=2&oqid=1513606863&atfLayout=list'.replace('stnb',keywords)
	get=getPage(sf).get()
	fbaurl="https://www.amazon.com/mn/search/ajax/gp/search/ref=sr_nr_p_85_0?fst=as%3Aoff&rh=i%3Aaps%2Ck%3Acd%2Cp_85%3A2470955011&keywords=cd&ie=UTF8&qid=1513394126&rnid=2470954011&fromHash=%2Fgp%2Fsearch%2Fref%3Dsr_nr_p_85_0%3Ffst%3Das%253Aoff%26rh%3Di%253Aaps%252Ck%253Acd%26keywords%3Dcd%26ie%3DUTF8%26qid%3D1513393836&section=ATF,BTF&fromApp=gp%2Fsearch&fromPage=results&fromPageConstruction=auisearch&version=2&oqid=1513397219&atfLayout=list"
	fbaurl=fbaurl.replace('cd',keywords)

	cd= getPage(fbaurl).get()
	# //*[@id="s-result-count"]/text()
	try:
		return (reSp(sctr(get) ),reSp(sctr(cd)))
	except Exception as e:
		print keywords
		keylog.info(keywords)
		return (0,0)

def reSp(AC):
	try:
		frant= re.split('of',str(AC))
		return  int( re.split('result',frant[1])[0].replace(",",""))
	except Exception as e:
		frant= re.split(r'>',str(AC))
		return  int( re.split('result',frant[1])[0].replace(",",""))

if __name__ == '__main__':
	print getTcumb('figit toys')



def getpageByason(asin,key):
	if asin.find('/dp/')>0:
		asin= asin.split('/')[3]		
	url ,Brand,review,Rank,reviewNumber,price,='https://www.amazon.com/dp/'+asin,'','','','',''
	page=getPage(url).get()
	Title =page[page.find('id="productTitle"'):].split('>')[1].split('<')[0]


	if page.find('class="a-size-medium a-color-price"')>0 and page.find('Currently unavailable')<0 :
		price=re.split(r'class="a-size-medium a-color-price',page)[1].split('>')[1].split('<')[0]

	if page.find('reviewCountTextLinkedHistogram noUnderline')>0:
		review=page[page.find('reviewCountTextLinkedHistogram noUnderline'):].split('"')[2]
		reviewNumber=page[page.find('acrCustomerReviewText'):].split('>')[1].split('<')[0]
	else :	
		review=0

	li= page.find('Best Sellers Rank')		

	if li!=-1:
		Rank= page[li:page.find('</td>',li)].replace('<span>','').replace('</th>','').replace('<td>','').replace('<br>','').replace('</span>','').replace('</td>','').replace(' ','').replace('\n',"")
	if page.find('Brand Name')>0:
		Brand=page[page.find("Brand Name"):].split('>')[2].split('<')[0]
	try:

		if key.find('-----')>0:
			amxpage.topKey.insert({'key':key,'asin':asin,'Title':Title,"Brand Name":Brand,"price": price.replace('$','').replace('\n','').replace(' ',''),"review":review,"reviewNumber":reviewNumber,'rank':Rank})
		else:
			amxpage.key.insert({'key':key,'asin':asin,'Title':Title,"Brand Name":Brand,"price": price.replace('$','').replace('\n','').replace(' ',''),"review":review,"reviewNumber":reviewNumber,'rank':Rank})
	except Exception as e:
		keylog.info(e)
def keTop(url,key):
	sqn=getPage(url).get()
	li=re.split(r'id=\"result_',sqn)  
	page= getPage('https://www.amazon.com/dp/'+li[2].split('"')[2]).get()	
	url= etree.HTML(page) .xpath('//*[@id="SalesRank"]/a/@href')[0]
	recursion(url,key)




def getli(url):
	sqn=getPage(url).get()
	otClass=sqn[sqn.find('<ul id="zg_browseRoot">'):]
 	return re.split('</li></ul>',otClass)[0].split("'")


def recursion(url,key):
 	li= getli(url)
 	re=0
 	sqn=''.join(getli(li[1])) 
	thread_list=[]			
 	if sqn.find(li[4])<0:
 		re=1
	lcount=len(li)/2
 	for x in xrange(lcount):
		
		url ,cv=li[x*2+1],x*2
		if x==0:cv=2
		re0= li[cv].replace('>','').split('<')[0]+ '-----' + key
		print re0
 		if re==1:
			pw = threading.Thread(target=recursion, args=(url,key,))
			thread_list.append(pw)
		pr = threading.Thread(target=fxBest, args=(url,key,))
		thread_list.append(pr)
	for jj in thread_list:
		jj.start()

def fxBest(url,key):
	thread_list ,li=[],[]
	st= re.split('a-link-normal zg_more_link',getPage(url).get())
	li.append(url)
	try:
		li.append(re.split('"',st[1])[2]) 
		li.append(re.split('"',st[2])[2])
	except Exception as e:
		keylog.info(e)

	for item in  li:
		pagefex (item,key,)
 


def pagefex(url ,key):
	count,	page ,thread_list= 0,getPage(url).get(),[]
	Title=	page[ page.find('zg_listTitle'):]
	Title= Title.split('>')[1].split('<')[0]+ Title.split('>')[2].split('<')[0]  +'-----'+key
	nextPagelist=re.split(r'ajaxUrl',page)

	for x in nextPagelist:
		if count!=0:
			page= getPage(x.split('"')[1]).get()
			print x.split('"')[1]
		li=re.split(r'zg_itemImmersion',page) 
		count +=1
		del li[0]
		print len(li)
		for item in  li:
			# print re.split("href",item)
			xz=re.split(r"href",item)
			# print len(xz)
 
			try:
				url=xz[1].split('"')[1]
			except Exception as e:
 				print item
			t =threading.Thread(target=getpageByason,args=(url,Title,))
			thread_list.append(t)
	for t in thread_list:
		t.start()






# if __name__ == '__main__':
# 	# fxBest('https://www.amazon.com/Best-Sellers-Sports-Outdoors-Fan-Darts-Dartboards/zgbs/sporting-goods/374850011/ref=zg_bs_nav_sg_4_375537011','test')
# 	# getAsinByUrl(
# 		# 'https://www.amazon.com/gp/search/ref=sr_ex_n_1?rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A172574%2Cn%3A9424016011%2Cn%3A172635%2Cp_6%3AATVPDKIKX0DER&bbn=172635&ie=UTF8&qid=1512609670'
# 		# ,' Printers & Accessories : Printers')
# 	# list=(
# 	# 	# 'https://www.amazon.com/s/ref=sr_nr_p_72_0?fst=as%3Aoff&rh=n%3A172282%2Cn%3A541966%2Ck%3Adell+desktop%2Cp_n_availability%3A1248801011%2Cp_72%3A1248879011&keywords=dell+desktop&ie=UTF8&qid=1505381005&rnid=1248877011',
# 	# 	# 'https://www.amazon.com/s/ref=sr_nr_p_n_availability_1?rh=n%3A172282%2Cn%3A541966%2Ck%3Alenovo+desktop%2Cp_72%3A1248882011%2Cp_n_availability%3A1248801011&keywords=lenovo+desktop&ie=UTF8&qid=1505358687',
# 	# 	# 'https://www.amazon.com/s/ref=sr_nr_p_n_availability_1?rh=n%3A172282%2Ck%3Aacer+laptop%2Cp_72%3A1248882011%2Cp_n_availability%3A1248801011&keywords=acer+laptop&ie=UTF8&qid=1505358746',
# 	# 	# 'https://www.amazon.com/s/ref=sr_nr_p_n_availability_1?rh=n%3A172282%2Ck%3Aacer+desktop%2Cp_72%3A1248882011%2Cp_n_availability%3A1248801011&keywords=acer+desktop&ie=UTF8&qid=1505358783',
#     #
# 	# 	# 'https://www.amazon.com/s/ref=sr_nr_p_n_availability_1?rh=n%3A172282%2Ck%3Aasus+laptop%2Cp_72%3A1248882011%2Cp_n_availability%3A1248801011&keywords=asus+laptop&ie=UTF8&qid=1505358843',
# 	# 	# 'https://www.amazon.com/s/ref=sr_nr_p_n_availability_1?rh=n%3A172282%2Ck%3Aasus+desktop%2Cp_72%3A1248882011%2Cp_n_availability%3A1248801011&keywords=asus+desktop&ie=UTF8&qid=1505358889',
# 	# 	# 'https://www.amazon.com/s/ref=sr_nr_p_n_availability_1?rh=n%3A172282%2Cn%3A541966%2Ck%3Aasus+desktop%2Cp_72%3A1248879011%2Cp_n_availability%3A1248801011&keywords=asus+desktop&ie=UTF8&qid=15054',
# 	# 	# 'https://www.amazon.com/s/ref=sr_nr_p_n_availability_1?rh=n%3A172282%2Ck%3Ahp+desktop%2Cp_72%3A1248879011%2Cp_n_availability%3A1248801011&keywords=hp+desktop&ie=UTF8&qid=1506392187',
#     #
# 	# 	)
# 	# key='assa'
# 	# stra= 'https://www.amazon.com/Best-Sellers-Industrial-Scientific/zgbs/industrial/ref=zg_bs_unv_indust_1_256167011_1'
# 	# recursion(stra,key)
# 	# page= getPage('https://www.amazon.com/dp/B018GSLFLU').get()	
# 	# re=	etree.HTML(page)
# 	# tcs=re.xpath('//*[@id="SalesRank"]/a/@href')
#  	# 	print tcs
# 	# cs=agetfanzle('http://www.fanzle.com/keywordscraper/load?q=crayons&s=0&p=0&l=0&g=com')
# 	# import json
# 	# for x in json.loads(cs.get())[1]:
# 	# 	print x
# 	getTcumb('cd')