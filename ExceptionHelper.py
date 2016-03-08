# -*- coding:UTF-8 -*-
'''~*~*~**~*~***~*~**~**~*~**~*~*~*~**~**~*~**~**~*~*~*~*~*~*~*
#  Author:Zhukang(zhukang@baidu.com)
# 
#  Abstract:Exception Handler
#
#  Created Time:2015-07-30
#  Copyright (c) 2014年 baidu. All rights reserved.
~*~*~**~*~***~*~**~**~*~**~*~*~*~**~**~*~**~**~*~*~*~*~*~*~*~*'''

class AssertionError(Exception):
	def __init__(self, info = ""):
		super(AssertionError, self).__init__()
		print("AssertionError:" + str(info))