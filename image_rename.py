#! /usr/bin/python

''' 
---------------------------------------------------------------------------------------------------------------------
Version python 3.9.2
Author: Nathaniel
Script usage:
	this is intended for renaming large groups of photos
	run script -> python by_date_rename.py 'date range by noting as: YEAR:MM:DD YEAR:MM:DD' 'new_name (no extension)'
Lib Details:
	Pillow library will need to be installed for script to work
	Reference -> pillow.readthedocs.io
Progress:
	Still working on script
---------------------------------------------------------------------------------------------------------------------
'''


import os
import sys
from PIL import Image
im = Image.open("Married.jpg").getexif()[36867]

#establishing current directory
current_directory = os.getcwd()

#declaring our argument values
if len(sys.argv) == 4:
	start_month = sys.argv[1]
	end_month = sys.argv[2]
	file_name = sys.argv[3]
	print("Initial Date: ", start_month, "\nFinal Date:", end_month, "\nName for File:", file_name)

#checks if the extension matches a image file extension
def checkExt(ext):
	ext = ext.lower() #insures all extensions are lowercase
	extensionList = ['.png', '.jpg', '.raw']
	isExt = False
	for n in extensionList:
		if ext == n:
			isExt = True
			if isExt:
				break
	return isExt
	
def str2int(dataList):
	for n in dataList[0]:
		n = int(n)
	for n in dataList[1]:
		n = int(n)
	return dataList

#splits up date string
def parseDateStr(dateStr):
	strHolder = ''
	data = dateStr.split(' ')
	date = strHolder.join(data[0])
	time = strHolder.join(data[1])
	date = date.split(':')
	time = time.split(':')
	dateTimeData = [date, time]
	#print(dateTimeData[1])
	str2int(dateTimeData)
	d = dateTimeData[0]
	j = d[0]
	print(type(j))

	return dateTimeData

#goes through director
for file in os.listdir(current_directory):
	tempFile = file
	fileName, fileExt = os.path.splitext(tempFile)

	if checkExt(fileExt):
		im = Image.open(file).getexif()[36867]
		print(file, im)
		parseDateStr(im)




