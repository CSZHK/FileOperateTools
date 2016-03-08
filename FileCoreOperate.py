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
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs
from ExceptionHelper import AssertionError
from FileInfo import FileInfo
SEP=os.path.sep
class FileCoreOperation:

    def getFileNameListFromPath(self,path):
        if path is None or path is "":
            raise AssertionError("文件路径为空！")
            return
        try:
            path.replace("/", SEP)
            print("os path:"+path)
            fileNameList=os.listdir(path)
            print("路径"+path+"的文件列表为:")
            print(fileNameList)
            return fileNameList
        except:
            print("文件不存在")

    def isDir(self,path):
        return os.path.isdir(path)

    def getDirAllFileAbsNameList(self,dir,fileList):
        if dir is None or dir is "":
            raise AssertionError(dir+":不是合法的路径！")
            return
        if self.isDir(dir):
            currentDirFileList=self.getFileNameListFromPath(dir)
            if currentDirFileList is None:
                return
            for eachFile in currentDirFileList:
                eachFileAbsPath=os.path.join(dir,eachFile)
                self.getDirAllFileAbsNameList(eachFileAbsPath,fileList)
        else:
            fileList.append(dir)

    def getCurrentDirAllFileAbsNameList(self):
        fileList=[]
        self.getDirAllFileAbsNameList(os.getcwd(),fileList)
        return fileList

    def getFileDetailInfo(self,absPath):
        if os.path.isfile(absPath) is False:
            return
        fileInfo=FileInfo(absPath);
        fileInfo.data=self.readFile2Data(absPath)
        print("文件名："+fileInfo.fileName+"'\n'")
        print("文件夹："+fileInfo.fileDir+"'\n'")
        print("总大小："+str(fileInfo.allSize)+"'\n'")
        print("数据大小："+str(len(fileInfo.data))+"'\n'")
        fileInfo.data=self.readFile2Data(absPath)
        return fileInfo


    def getDirAllFileInfo(self,dir):
        if self.isDir(dir) is False:
            raise AssertionError(dir+":不是合法的路径！")
            return 
        fileInfoList=[]
        self.getDirAllFileAbsNameList(dir,fileInfoList)
        if fileInfoList is None:
            AssertionError(dir+":目录下面没有文件！")
            return
        for eachFileName in fileInfoList:
            fileInfo=self.getFileDetailInfo(eachFileName)
            fileInfoList.append(fileInfo)
        return fileInfoList


    #打开文件   
    def open(self):
        try:
            self.fileOut = codecs.open(self.out,'w','utf-8')
        except IOError as err:
            print('File err:' + str(err))

    #关闭文件       
    def close(self):
        if self.fileOut is not None:
            self.fileOut.close()

    def readFile2Data(self,fileAbsPath):
        try:
            with codecs.open(fileAbsPath, 'r', 'utf-8') as javafile:
                data = javafile.read() 
                javafile.close()
                return data 
        except IOError as err:
            print('File err:' + str(err))
            raise AssertionError('File err:' + str(err)) 

    def readFileAllLines(self,fileAbsPath):
        try:
            with codecs.open(fileAbsPath, 'r', 'utf-8') as javafile:
                lines = javafile.readlines();
                javafile.close()
                return lines 
        except IOError as err:
            print('File err:' + str(err))
            raise AssertionError('File err:' + str(err))  

    def readFileInfo(self,fileAbsPath,info):
         try:
            with codecs.open(fileAbsPath, 'r', 'utf-8') as javafile:
                lines = javafile.readlines();
                if info is None:
                    info = self.getFileDetailInfo(fileAbsPath)
                info.fileLines = lines
                javafile.close()
                return info 
         except IOError as err:
            print('File err:' + str(err))
            raise AssertionError('File err:' + str(err))  

    #获取文件类型
    def getFileType(self,fileAbsPath):
        list = os.path.splitext(fileAbsPath)
        if len(list)>1:
            return list[1]
        else:
            return ""

    #获取文件名
    def getFileName(self,fileAbsPath):
        return os.path.basename(fileAbsPath)











        





    


        
