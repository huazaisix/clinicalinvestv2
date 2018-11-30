#!/usr/bin/python
#coding=utf-8

from utils.read_file_util import readexcel
import xlrd 
import json

#录入一般情况
def readGeniralInfo(file, dictname):
	sheet0 = file.sheets()[0]
	sheet1 = file.sheets()[1]
	#基本信息，1~5项
	readexcel.readStrInfoToDict(sheet0, dictname, 4, 1, 2, 9)
	#年龄身高
	readexcel.readIntInfoToDict(sheet0, dictname, 4, 1, 9, 11)
	# 血型民族
	readexcel.readStrInfoToDict(sheet0, dictname, 4, 1, 12, 15)
	#体重
	readexcel.readFloatInfoToDict(sheet0, dictname, 4, 1, 11, 12)
	#6.特殊工作环境
	readexcel.readBoolInfoToDict(sheet1, dictname, 1, 2, 1, 9)
	#7~10项
	readexcel.readStrInfoToDict(sheet0, dictname, 4, 1, 24, 28)
	#11.饮食偏好
	readexcel.readBoolInfoToDict(sheet1, dictname, 4, 5, 1, 11)
	
	
#录入月经情况
def readMenstruationInfo(file, dictname):	
	sheet = file.sheets()[0]
	#1项
	readexcel.readIntInfoToDict(sheet, dictname, 4, 1, 40, 41)
	#2项（规律为True则使用key：normal，否则使用key：abnormal）
	readexcel.readBoolInfoToDict(sheet, dictname, 4, 1, 42, 43)
	if sheet.cell(42, 1).value == True:
		dictname["normal"] = sheet.cell(43, 1).value
	else:
		dictname["abnormal"] = sheet.cell(44, 1).value
	#3~8项
	readexcel.readStrInfoToDict(sheet, dictname, 4, 1, 45, 51)
	

#录入全身症状
def readSymptomInfo(file, dictname):	
	sheet = file.sheets()[2]
	#精神
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 1, 8)
	#情绪
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 11, 21)
	#寒热
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 24, 29)
	#出汗
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 32, 39)
	#语音
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 42, 46)
	#面色
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 49, 62)
	#心
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 65, 68)
	#乳房
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 71, 76)
	#胸胁
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 79, 83)
	#腰膝
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 86, 92)
	#腹部 
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 95, 105)
	#头
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 108, 112)
	#目
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 115, 122)
	#耳
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 125, 128)
	#咽喉
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 131, 136)
	#口味
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 139, 147)
	#饮食
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 150, 160)
	#睡眠	
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 163, 170)
	#大便
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 173, 181)
	#小便
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 184, 194)
	#四肢
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 197, 205)
	#其他
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 208, 211)
	#舌质
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 214, 220)
	#舌苔
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 223, 236)
	#舌体
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 239, 244)
	#脉象
	readexcel.readBoolInfoToDict(sheet, dictname, 1, 2, 247, 264)
	
	
#录入其他
def readOtherInfo(file, dictname):	
	sheet0 = file.sheets()[0]
	sheet3 = file.sheets()[3]
	#----个人史
	# 1.出生情况
	readexcel.readBoolInfoToDict(sheet3, dictname, 25, 26, 1, 5)
	# dictname["person_born"] = "足月产"
	#2.特殊嗜好
	readexcel.readBoolInfoToDict(sheet3, dictname, 1, 2, 1, 5)
	#3~6项
	readexcel.readStrInfoToDict(sheet0, dictname, 4, 1, 116, 121)
	#减肥情况
	#“有”则包含运动减肥等参数，“无”则没有这些键值对
	if sheet0.cell(120, 1).value == "有":
		dictname["reducefat_ever"] = True
		readexcel.readBoolInfoToDict(sheet3, dictname, 4, 5, 1, 4)	
		#“其他”方式不填写则默认为“无”		
		if sheet0.cell(125, 1).ctype == 0:
			dictname["reducefat_qita"] = "无"
		else:
			dictname["reducefat_qita"] = sheet0.cell(125, 1).value
		readexcel.readIntInfoToDict(sheet0, dictname, 4, 1, 126, 127)	
	else:
		dictname["reducefat_ever"] = False
	#7.经期情况
	readexcel.readStrInfoToDict(sheet0, dictname, 4, 1, 128, 132)
	#8.平素带下情况
	readexcel.readBoolInfoToDict(sheet3, dictname, 7, 8, 1, 9)
	#9.既往病史
	readexcel.readBoolInfoToDict(sheet3, dictname, 10, 11, 1, 17)
	#---月经不调病史
	readexcel.readBoolInfoToDict(sheet3, dictname, 13, 14, 1, 8)
	#---家族史
	#一级亲属疾病史
	readexcel.readStrInfoToDict(sheet0, dictname, 4, 1, 133, 135)
	#一级亲属其他疾病史
	readexcel.readBoolInfoToDict(sheet3, dictname, 16, 17, 1, 7)
	#一级亲属其他疾病史最后一项其他
	dictname["reducefat_qita"] = "无"
	#---孕育史
	readexcel.readStrInfoToDict(sheet0, dictname, 4, 1, 144, 154)
	#---避孕措施
	readexcel.readBoolInfoToDict(sheet3, dictname, 19, 20, 1, 5)
	print(sheet3.cell(4, 20).value)
	if sheet3.cell(4, 20).value == True:
		#末次口服避孕药时间
		print(sheet0.cell(160, 1).value)
		readexcel.readFloatInfoToDict(sheet0, dictname, 4, 1, 160, 161)
		#避孕药
		readexcel.readBoolInfoToDict(sheet3, dictname, 22, 23, 1, 6)
		#“其他”方式不填写则默认为“无”		
		if sheet0.cell(167, 1).ctype == 0:
			dictname["reducefat_qita"] = "无"
		else:
			dictname["reducefat_qita"] = sheet0.cell(125, 1).value		
	#---相关辅助检查
	readexcel.readStrInfoToDict(sheet0, dictname, 4, 1, 169, 179)
	#“其他”方式不填写则默认为“无”		
	if sheet0.cell(167, 1).ctype == 0:
		dictname["accessory_qita"] = "无"
	else:
		dictname["accessory_qita"] = sheet0.cell(179, 1).value	

	
#录入临床诊断
def readConclusionInfo(file, dictname):
	sheet0 = file.sheets()[0]
	sheet4 = file.sheets()[4]	
	#---中医诊断
	readexcel.readBoolInfoToDict(sheet4, dictname, 1, 2, 1, 6)	
	#---辨证分型
	#1.虚证
	readexcel.readBoolInfoToDict(sheet4, dictname, 4, 5, 1, 11)
	dictname["qita_asthenic"] = ""
	#“其他”方式不填写则默认为“无”		
	'''
	if sheet0.cell(167, 1).ctype == 0:
		dictname["qita_asthenic"] = "无"
	else:
		dictname["qita_asthenic"] = "待修改"	
	'''
	#2.实证
	readexcel.readBoolInfoToDict(sheet4, dictname, 7, 8, 1, 11)
	#“其他”方式不填写则默认为“无”	
	dictname["qita_demonstration"] = ""
	'''	
	if sheet0.cell(167, 1).ctype == 0:
		dictname["qita_demonstration"] = "无"
	else:
		dictname["qita_demonstration"] = "待修改"	
	'''
	#3.虚实夹杂证
	readexcel.readBoolInfoToDict(sheet4, dictname, 10, 11, 1, 8)
	#“其他”方式不填写则默认为“无”	
	dictname["qita_def_ex"] = ""
	'''	
	if sheet0.cell(167, 1).ctype == 0:
		dictname["qita_def_ex"] = "无"
	else:
		dictname["qita_def_ex"] = "待修改"
	'''
	#---西医诊断
	readexcel.readBoolInfoToDict(sheet4, dictname, 13, 14, 1, 4)
	readexcel.readStrInfoToDict(sheet0, dictname, 4, 1, 204, 205)

	
def readQuestionaireExcel(excelfilepath, jsonfilepath=None):
    xlsmfile = xlrd.open_workbook(excelfilepath)
    # jsonfile = open(jsonfilepath, mode='w')

    general_dict = {}
    menstruation_dict = {}
    symptom_dict = {}
    other_dict = {}
    conclusion_dict = {}

    output_dict = {"general_info": general_dict, "menstruation": menstruation_dict, "symptom": symptom_dict, "other": other_dict, "conclusion": conclusion_dict}

    readGeniralInfo(xlsmfile, general_dict)
    readMenstruationInfo(xlsmfile, menstruation_dict)
    readSymptomInfo(xlsmfile, symptom_dict)
    readOtherInfo(xlsmfile, other_dict)
    readConclusionInfo(xlsmfile, conclusion_dict)

    jsondata = json.dumps(output_dict)
    print(jsondata)

    return jsondata
