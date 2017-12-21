from flask import Flask
import sys
sys.path.append('../')
from db.mysql import db_mysql


dbco=db_mysql()
app = Flask(__name__)



@app.route('/selectAsin/<asin>')
def selectAsin(asin):
	sql='select *from SearchWords where asin='+asin
	return dbco.seclet(sql)
@app.route('/selectTi/<ti>')
def selectti(ti):
	sql='select *from SearchWords where Title like %'+ti
	return dbco.seclet(sql)

@app.route('/selectkeyword/<key>')
def select(key):
	sql='select *from beauty where Keywords ='+key
	return dbco.seclet(sql)

@app.route('/selectkeywordlike/<key>')
def selectkeywordlike(key):
	sql='select *from beauty where Keywords like %'+key
	return dbco.seclet(sql)
if __name__ == '__main__':
	app.run()