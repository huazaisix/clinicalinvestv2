#!/usr/bin/python
#coding=utf-8

import xlrd 
from datetime import datetime
from xlrd import xldate_as_tuple

"""
录入布尔数据
参数:xls文件工作表、录入字典名、参数列、参数对应数值列、起始行、终止行
"""
def readBoolInfoToDict(currentsheet, dictname, paracolno, valuecolno, startrowno, endrowno):
	nrows = currentsheet.nrows
	i = 1
	for i in range(startrowno,endrowno):
		cell1 = currentsheet.col(paracolno)[i].value
		ctype2 = currentsheet.col(valuecolno)[i].ctype		
		if ctype2 == 0:
			cell2 = False
		elif ctype2 == 4:
			cell2 = bool(currentsheet.col(valuecolno)[i].value)
		else:
			cell2 = False
		dictname[cell1] = cell2
		i = i+1	
	return

	
"""
录入字符串数据
参数:xls文件工作表、录入字典名、参数列、参数对应数值列、起始行、终止行
"""	
def readStrInfoToDict(currentsheet, dictname,  paracolno, valuecolno, startrowno, endrowno):
	nrows = currentsheet.nrows
	i = 1
	for i in range(startrowno,endrowno):
		cell1 = currentsheet.col(paracolno)[i].value
		ctype2 = currentsheet.col(valuecolno)[i].ctype	
		tmp = currentsheet.col(valuecolno)[i].value	
		#单元格为空，则默认为“无”
		if ctype2 == 0:
			cell2 = "无"		
		elif ctype2 == 2: 
			cell2 = int(tmp)	
			cell2 = str(cell2)
		#单元格格式为日期，则转换成%Y/%d/%m格式的字符串
		elif ctype2 == 3:
			data = datetime(*xldate_as_tuple(tmp, 0))
			cell2 = data.strftime('%Y/%d/%m')
		else:
			cell2 = str(tmp)
		dictname[cell1] = cell2
		i = i+1	
	return

	
"""
录入整数数据
参数:xls文件工作表、录入字典名、参数列、参数对应数值列、起始行、终止行
"""	
def readIntInfoToDict(currentsheet, dictname,  paracolno, valuecolno, startrowno, endrowno):
	nrows = currentsheet.nrows
	i = 1
	for i in range(startrowno,endrowno):
		cell1 = currentsheet.col(paracolno)[i].value
		ctype2 = currentsheet.col(valuecolno)[i].ctype	
		tmp = currentsheet.col(valuecolno)[i].value	
		#单元格为空，则默认为0		
		if ctype2 == 0:
			cell2 = 0
		elif ctype2 == 2: 
			cell2 = int(tmp)			
		else:
			cell2 = 0
		dictname[cell1] = cell2
		i = i+1	
	return

"""
录入浮点数数据
参数:xls文件工作表、录入字典名、参数列、参数对应数值列、起始行、终止行
"""	
def readFloatInfoToDict(currentsheet, dictname,  paracolno, valuecolno, startrowno, endrowno):
	nrows = currentsheet.nrows
	i = 1
	for i in range(startrowno,endrowno):
		cell1 = currentsheet.col(paracolno)[i].value
		ctype2 = currentsheet.col(valuecolno)[i].ctype	
		tmp = currentsheet.col(valuecolno)[i].value	
		#单元格为空，则默认为0		
		if ctype2 == 0:
			cell2 = 0
		elif ctype2 == 2: 
			cell2 = tmp			
		else:
			cell2 = 0
		dictname[cell1] = cell2
		i = i+1	
	return
	