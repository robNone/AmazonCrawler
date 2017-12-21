# -*- coding: utf-8 -*-

from __future__ import unicode_literals


import requests ,sys,time
sys.path.append('../')
from  getProxy.manipulateProxy  import get ,delet
from LogHandler import LogHandler
reqErro=LogHandler('neterro',stream=False)

class request(object):
	"""docstring for request"""
	def __init__(self,data):
		super(request, self).__init__()
		self.data = data
	def judge(self):
		if self.data['url'].find('https://www.amazon.com')<0:
	 		self.data['url']='https://www.amazon.com/'+self.data['url']
	def cport(self):
		port = get()
	 	return { "http": "http://" + port, "https": "http://" + port, }
	def webGet(self):
	 	try:
	 		proxies=[]
	 		if self.data['ac']==None:
	 			self.judge()
	 			proxies=self.cport()
	 		# print self.data['url']
	 		print self.data['url']
			re = requests.get(url=self.data['url'],headers=self.data['headers'],timeout=self.data['timeout'], proxies=proxies )
			print (re.status_code)
			if re.text.find('Robot Check')>0 or (re.status_code!=200 and re.status_code!=404 )   :
				reqErro.info('Robot Check')
				return None
			else :
				return re
		except Exception as e:
			reqErro.info(e)
			print e
			return None
 

			
	def webPost(self):
	 	try:
			re = requests.post(url=self.data['url'],
	                      headers=self.data['headers'],timeout=self.data['timeout'],data=self.data['data'],verify=False )
			print  (re.status_code)
			if re.text.find('Robot Check')>0 or re.status_code!=200:
				return None
			else :
				return re
		except Exception as e:
			print (e)
			return None
	def doerro(self):
		de = None
		while de == None:
			if self.data.has_key('data'):
				de = self.webPost() 
			else:
				de = self.webGet()
			if de != None:
				break
		print (self.data['url'] + ' go......Success')
		# de..encode("UTF-8") ?
		return de.text
	# def getPort(self):
	# 	ret =''
	# 	while ret=='':
	# 		try:
	# 			ret= requests.get('http://www.66ip.cn/getzh.php?getzh=2017082128640&getnum=1&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=0&proxytype=1&api=https').text.replace('<br>','').replace('	','').replace(' ','').replace('\r','').replace('\n','').replace('\t','')
	# 		except Exception as e:
	# 			print e
		# return ret


if __name__ == '__main__':
	headers ={ 
# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
# 	    	"Accept-Language":"zh-CN,zh;q=0.8",
# 	    	# "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
# "Referer":"https://ipcrs.pbccrc.org.cn/",
# "Host":"ipcrs.pbccrc.org.cn",
# # "X-Requested-With":"XMLHttpRequest",
# "Connection":"keep-alive",
# "Upgrade-Insecure-Requests":"1",
# "Cookie":"BIGipServerpool_ipcrs_app=ftZcycNISrv19FgF9TwayuIh5sFUdlx6XDWLbHZHLaZuv71B1WxkLagO5xaZrwKI097mcndFBVkLHOG3/2ObbRzSorDONuGGx92MugnLSfeWo5Eem/jcCTlWuCac4IWrwjAswf23rtfyVA8F+f3lC4+WQqGoFA==; BIGipServerpool_ipcrs_web=FUzObDhBBNQN6bwF9TwayuIh5sFUdsLcEsqBY/YKYwHYCizig5nnLhwYUdQbe81FEpHaWfvluKvq; JSESSIONID=zDQfZLvYd1jrn82yTR2HyJDLL9HlBv9ljXQbLyL4WHhCGhpdQgGh!-949863470; TSf75e5b=206623ee0b4ce21ed9af4468dd627e22660c57e0b25101fe59c8a251",
# "Origin":"https://ipcrs.pbccrc.org.cn"

      'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN',

# "Cookie":"BIGipServerpool_ipcrs_app=ftZcycNISrv19FgF9TwayuIh5sFUdlx6XDWLbHZHLaZuv71B1WxkLagO5xaZrwKI097mcndFBVkLHOG3/2ObbRzSorDONuGGx92MugnLSfeWo5Eem/jcCTlWuCac4IWrwjAswf23rtfyVA8F+f3lC4+WQqGoFA==; BIGipServerpool_ipcrs_web=FUzObDhBBNQN6bwF9TwayuIh5sFUdsLcEsqBY/YKYwHYCizig5nnLhwYUdQbe81FEpHaWfvluKvq; JSESSIONID=zDQfZLvYd1jrn82yTR2HyJDLL9HlBv9ljXQbLyL4WHhCGhpdQgGh!-949863470; TSf75e5b=8f7af5e2b21ec9d028716a6d6ab47652660c57e0b25101fe59c8ab3f"


}
	headers ={
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
	        "Host":"www.amazon.com",
	    	"Accept-Language":"zh-CN,zh;q=0.8",
"Cookie":	'aws-target-static-id=1497838335626-19381; s_vn=1529374335856%26vn%3D1; regStatus=pre-register; aws_lang=cn; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1497838335629-9703.24_4; amznacsleftnav-1e4dfe77-0d78-3527-b54a-f23cc2cb231e=1; AMCVS_4A8581745834114C0A495E2B%40AdobeOrg=1; AMCV_4A8581745834114C0A495E2B%40AdobeOrg=-894706358%7CMCIDTS%7C17415%7CMCMID%7C15071633912452894915662900002460765377%7CMCOPTOUT-1504585615s%7CNONE%7CMCAID%7C2CD68D00852A8569-40000301C00003C7%7CvVersion%7C2.3.0; s_lv=1504578420898; appstore-devportal-locale=zh_CN; s_vnum=1931133517751%26vn%3D4; s_nr=1504749318700-Repeat; s_dslv=1504749318701; s_ppv=85; at-main=Atza|IwEBIDDWvxoMHsifLiTWazK1cSAb6sPs44jFlHu4oL3LodNKVsU8NGdSm5K8FdmMWr__wQDtiusZ88pZrsaXKPN42AIgcztHnSaeYEUHhgy0P3sil04wpCLe2F1m_HK7eZDg0D6bxXBzGOttA8lN4Um0cObimx2j07DNb1KHtgA465FpjPDMqWfHdw_Uvy4vKwfqIzwSp2nO3iqK1VlRDQlcNCHFi33PfESso3Up1yHvkhiqBlVSVl-GSm7a49vnTMX-xGIhPWqDBCSEunEF8nPTZ1Y4zM0RCnQojWjaCiesNq_3iy3PgL-LKEEmxTNe6RixwK3d2Swd8dWjcy743XEdxa4xUeiD9wtrT8Zx0hyWIYejSDm7W0REBeViHrYNw8Pr927I5Vrlm6rN23psIff2--yF; sess-at-main="goK1tVYcgb7R2XcYasQ8/+2ABnZO2hdIYIDDrbHkOiM="; x-wl-uid=1XXT7ohIeJZyY/7sC/ytnTHT+Vwn62xt/Jqr4l2xe+WetZvII2HlOUcCgEXfKRBNwgbOTZrrdaMcZJNwjXVH48GrQ2/ROuA6CLbVJ1xZ9Jo0PgAxPQ9L1NbmGgdG1oBrv+QyImd7kzKk=; skin=noskin; JSESSIONID=5AF6FA51D68211D42C8B1E4F272968D3; s_sess=%20s_ppvl%3D%3B%20s_ppv%3DUS%25253AAZ%25253ASOA-overview-seeall%252C92%252C37%252C3448%252C2880%252C1348%252C1920%252C1080%252C0.67%252CL%3B%20s_cc%3Dtrue%3B%20c_m%3DundefinedTyped/BookmarkedTyped/Bookmarked%3B%20s_sq%3Dacsus-prod%253D%252526pid%25253D508510%252526pidt%25253D1%252526oid%25253Dhttps%2525253A%2525252F%2525252Fwww.amazon.com%2525252Fgp%2525252Fhelp%2525252Fcustomer%2525252Fforums%2525252Fkindleqna%2525252Fref%2525253Dhp_gt_comp_ss_forum_Kindle%252526ot%25253DA%3B; s_pers=%20s_fid%3D0B584A252E26D24B-0508DABA67938BE2%7C1662514482807%3B%20s_dl%3D1%7C1507518928552%3B%20gpv_page%3DUS%253ASC%253A%2520SellerCentralLogin%7C1507518928555%3B%20s_ev15%3D%255B%255B%2527Typed/Bookmarked%2527%252C%25271507517128514%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271507517128557%2527%255D%255D%7C1665283528557%3B; x-main="Ihat36AUznBqU@bAXSLMRPKxSgCxnH1bEUQiqvtsIVRnH75aplq29jnQqj?LHESj"; lc-main=en_US; session-token="STQf3qhsr7tRS9RXdV+B5iLxVuHXTWxw3sz5jRhYxXQ8OePnWMVSkTiU5Wot7+yBX2/sYgnK2b585EUmLISbef7iNSg9mAtKSxMrAgH3WlNomIsvZw5cciATBtgld6xxTLN0L4qRqPXGW6ucpWuX9M0yI4EWddIswJKbCJK56B27pyn72QR0wPvzVVODwGZRxTxjBywnAJfXhbq/zyaIytgH0BvgASM5FAp6FyMVO7E/dq31m2t0EQY1Jx+jmFu6/mZy03RzzDPWKOZKlpVMSg=="; ubid-main=131-0601013-2724535; session-id-time=2082787201l; session-id=136-1823294-1208816; csm-hit=TC76C8PW39N5MY6AKGWM+s-FTFB6ESPHJ74V4N2XPGW|1507777709001'

            }
	data={

"org.apache.struts.taglib.html.TOKEN":"80e8e763d3b8bbbbb16acfa34c403c95",
"method":"login",
"date":"1506323412195",
"loginname":"1634475170",
"password":"1634475170Q",
"_@IMGRC@_":"csn9gi",


}

	r = request({'url':'https://www.amazon.com/Best-Sellers-Home-Improvement-Air-Powered-Tools/zgbs/hi/552684/ref=zg_bs_nav_hi_1_hi','headers':headers,'timeout':3,})
	s= r.doerro()
	print  s
