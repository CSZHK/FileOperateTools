import os
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
from FileWritter import FileWritter
from AndroidProjectOperate import AndroidProjectOperate

class Main:
	def __init__(self):
		self.operate=AndroidProjectOperate()
		self.checkStringRes()
		

	def checkStringRes(self):
		self.operate.start()

Main();
		

	

   
