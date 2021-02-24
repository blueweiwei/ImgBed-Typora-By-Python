#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#  Copyright 2021 ������ <������@DESKTOP-03B3450>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import leancloud
import sys
import re


def log(content):
	print(str(content))

def matchName(upurl):
    # 正则匹配
	reg = r'[^\\/:*?"<>|\r\n]+$'
	filename= re.findall(reg,upurl)
	return filename[0]

def uplean(upurl,filename):
    # leancloud 密钥 上传文件代码
	# leancloud密钥
	leancloud.init("<您的AppID>","<您的appKey>")
	with open(upurl, 'rb') as f:
		file = leancloud.File(filename,f)
		files=file.save()
		return file._url

if __name__ == '__main__':
	# 读取传入的字符串
	
	# test 数据
	# teststr = ['0', r"C:\Users\天琼懵\Pictures\index.jpg"]
	# for file in teststr[1:]:
	for file in sys.argv[1:]:
			# print(file)
			filename=matchName(file)
			# print(filename)
			url=uplean(file,filename)
			print(url)
	
	
	
	

