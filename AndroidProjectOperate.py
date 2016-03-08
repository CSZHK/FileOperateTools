# -*- coding:UTF-8 -*-
'''~*~*~**~*~***~*~**~**~*~**~*~*~*~**~**~*~**~**~*~*~*~*~*~*~*
#  Author:Zhukang(zhukang@baidu.com)
# 
#  Abstract:Exception Handler
#
#  Created Time:2016-1-29
#  Copyright (c) 2014年 baidu. All rights reserved.
~*~*~**~*~***~*~**~**~*~**~*~*~*~**~**~*~**~**~*~*~*~*~*~*~*~*'''
import os
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
from FileCoreOperate import FileCoreOperation
from FileInfo import FileInfo
from AndroidResInfo import AndroidResInfo
from FileWritter import FileWritter
class AndroidProjectOperate:
    def __init__(self):
    	self.sourceDir=[]
    	self.allFileList=[]
    	self.stringXmlList=[]
    	self.stringXmlDataList=[]
    	self.stringNameList=[];
    	self.stringDuplyNameDic={}
    	self.fileCoreOperate=FileCoreOperation()
    	self.writter=FileWritter()
    	self.outPath=""

    def readConfig(self):
    	fileList = self.fileCoreOperate.getCurrentDirAllFileAbsNameList()
    	for eachFileName in fileList:
            if "Config" in eachFileName:
                print("readConfig")
                self.sourceDir=self.fileCoreOperate.readFileAllLines(eachFileName)
                break


    def getAllAndroidProjectFileNameList(self,path):
    	for eachDir in self.sourceDir:
            print("config dir:"+eachDir)
            eachDir = eachDir.strip()
            self.fileCoreOperate.getDirAllFileAbsNameList(eachDir,self.allFileList)

    def getAllStringXmlFileList(self):
    	for eachFile in self.allFileList:
    		if eachFile is None or eachFile is "":
    			continue 
    		if "strings" in eachFile  and self.fileCoreOperate.getFileType(eachFile)==".xml":
    			self.stringXmlList.append(eachFile)

    def getAllStringXmlFileDataList(self):
    	for eachFile in self.stringXmlList:
    		if eachFile is None or eachFile is "":
    			continue
    		info = self.fileCoreOperate.readFileInfo(eachFile,None)
    		for eachLine in info.fileLines:
    			if eachLine is None or "":
    				continue
    			stringName = self.getStringName(eachLine)
    			if stringName is None or "":
    				continue
    			resInfo = AndroidResInfo()
    			resInfo.currentLine = eachLine
    			resInfo.key=stringName
    			resInfo.fileInfo=info
    			self.processStringName(stringName,resInfo)

    def getStringName(self,str):
    	if str is None or str is "":
    		return ""
    	start=str.find(">")
    	end=str.find("</")
    	if start>0 and end>start+1:
            stringName=str[start+1:end]
            stringName = stringName.strip("\n")
            return stringName
    	return ""

    def processStringName(self,stringName,resInfo):
    	if stringName is None or "":
    		return
    	ResInfoList = self.stringDuplyNameDic.get(stringName, None) 
    	if ResInfoList is None:
    		ResInfoList = []
    	ResInfoList.append(resInfo)
    	self.stringDuplyNameDic[stringName] = ResInfoList
    		##如果String名字在已有列表中，表明重复
    	if stringName not in self.stringNameList:
    		self.stringNameList.append(stringName)

    def printDuplyStringInfo(self):
        self.readOutPath()
        self.writter.outFile=self.outPath
        self.writter.open()
        if self.stringDuplyNameDic is not None:
            for eachKey in self.stringNameList:
                if eachKey.strip() is None or "":
                    continue
                if len(eachKey)==0:
                    continue
                resInfoList = self.stringDuplyNameDic.get(eachKey, None)
                if len(resInfoList) < 2:
                    continue
                self.writter.write("字符串值： "+eachKey+"\n")
                for eachRes in resInfoList:
                    if eachRes is not None:
                        self.writter.write("所在行： "+eachRes.currentLine.replace("\n", "")+"\n")
                        if eachRes.fileInfo is not None:
                            self.writter.write("所在路径： "+eachRes.fileInfo.absPath.replace("\n", "")+"\n")
                self.writter.write("\n")
        self.writter.close()

    def readOutPath(self):
        for eachLine in self.sourceDir:
            if "outPath=" in eachLine:
                strList = eachLine.split("\"")
                if len(strList)>1:
                    self.outPath=strList[1]
                    break
		

    def start(self):
    	self.readConfig()
    	self.getAllAndroidProjectFileNameList("")
    	self.getAllStringXmlFileList()
    	self.getAllStringXmlFileDataList()
    	self.printDuplyStringInfo()



	

			




