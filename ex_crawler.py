'''
#File Name:	ex_crawler.py
#File Disc:	how to crawler one web address
#Other:		title only
#Date:		2013/01/xx
'''
import urllib2
import re
import io
import sys

web_type = sys.getfilesystemencoding()
url = 'http://book.sfacg.com/Novel/31979/61619/410355/'
req = urllib2.Request(url)
html_src = urllib2.urlopen(req).read().decode('utf-8').encode(web_type)

title = re.findall('<div class="list_menu_title".+>(.+)</div>', html_src)[0]
print title