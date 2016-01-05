'''
#File Name:	ex_sql.py
#File Disc:	how connect mysql with python
#Author:	yuki
#Date:		2015/12/15
'''
# -*- coding: utf-8 -*-
import MySQLdb	#mysql database
import urllib2	#catch web
import io
import re
import sys
import os

if len(sys.argv) < 2:
	print 'No Argument'
	print 'python ex_sql.py pixnet_url'
	sys.exit()
else:
	reqtype = sys.getfilesystemencoding()	#to known system coding type(charset)
	#print reqtype
	web_addr = sys.argv[1]
	url = urllib2.Request(web_addr)
	html_src = urllib2.urlopen(url).read().decode('utf-8').encode(reqtype)
	article_ID = re.findall('/post/(.+)">', html_src)[0]
	#print article_ID
	title = re.findall('<h2><a href=.*>(.+)</a></h2>', html_src)[0]
	title = title.decode('Big5')

	#execute mysql language
	db = MySQLdb.connect(host='localhost', user='root', passwd='', db='', port=3306, charset='utf8')
	cur = db.cursor()	
	cmd = "insert into article (artID, title) values (%s, %s)"	#sql command
	cur.execute(cmd, (article_ID, title))
	db.commit()	#if db change, must commit
	db.close()
