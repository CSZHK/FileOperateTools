# -*- coding:UTF-8 -*-
'''~*~*~**~*~***~*~**~**~*~**~*~*~*~**~**~*~**~**~*~*~*~*~*~*~*
#  Author:Zhukang(zhukang@baidu.com)
# 
#  Abstract:Exception Handler
#
#  Created Time:2015-07-30
#  Copyright (c) 2014年 baidu. All rights reserved.
~*~*~**~*~***~*~**~**~*~**~*~*~*~**~**~*~**~**~*~*~*~*~*~*~*~*'''
import os
class FileInfo:
	def __init__(self):
		self.absPath=""
		self.fileName = ""
		self.fileDir= ""
		self.allSize = 0
		self.data = ""
		sefl.dataSize=0
		self.fileLines={}

	def __init__(self,absPath):
		self.absPath=absPath
		self.fileName = ""
		self.fileDir = ""
		self.allSize = 0
		self.data = ""
		self.dataSize = ""
		self.fileLines={}
		self.parserFileInfo()


	def parserFileInfo(self):
		self.fileName=os.path.basename(self.absPath)
		self.fileDir=os.path.dirname(self.absPath)
		self.allSize=os.path.getsize(self.absPath)


		