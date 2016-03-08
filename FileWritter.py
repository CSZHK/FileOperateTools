import codecs

import os
SEP = os.path.sep
class FileWritter:
	def __init__(self):
		self.fileOut=""
		self.outFile=""

	def open(self):
		try:
			self.fileOut = codecs.open(self.outFile,'w','utf-8')
		except IOError as err:
			print('File err:' + str(err))

	
	def close(self):
		if self.fileOut is not None:
			self.fileOut.close()

	def write(self,value_write):
		self.fileOut.write(value_write)