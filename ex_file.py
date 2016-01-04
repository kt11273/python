'''
#File Name:	ex_file.py
#File Disc:	write data to a file
#Author:	yuki
#Date:		2015/12/15
'''
# -*- coding: utf-8 -*-
import urllib2
import io
import re			
import sys

#catch web data
web_addr = 'http://danny0425.pixnet.net/blog/post/441113254'
url = urllib2.Request(web_addr)
html_src = urllib2.urlopen(url).read().decode('utf-8').encode('utf-8')

author_ID = re.findall('http://(.+).pixnet.net', html_src)[0]
article_ID = re.findall('/post/(.+)">', html_src)[0]
title = re.findall('og:title" content="(.+) @', html_src)[0]
print 'title: ' + title.decode('utf-8')
content = re.findall('<p.*><span.*;">(.+)</span></p>', html_src)

#write to file
filename = str(article_ID)+'.txt'
	#(path/)filename
FH = open(filename, 'w')

FH.writelines(author_ID)
FH.write('\n')
FH.writelines(title)
FH.write('\n')

#write file with 'list' (two version)
#while version
num = 0
while num < len(content):
	FH.write(content[num])
	FH.write('\n')
	num += 1

'''
#for version
for num in range(len(content)):
	FH.write(content[num])
	FH.write('\n')
'''
FH.close()