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
---------------------------------------------------------------------------------------------------------------------
'''

import os
import sys
from PIL import Image
#im = Image.open("Married.jpg").getexif()[36867]
  
#establishing current directory
current_directory = os.getcwd()

start_month = ''
end_month = ''
file_name = ''

#declaring our argument values
if len(sys.argv) == 4:
	start_month = sys.argv[1]
	end_month = sys.argv[2]
	file_name = sys.argv[3]
	print("Initial Date: ", start_month, "\nFinal Date:", end_month, "\nName for File:", file_name)
else:
	print('Incorrect Input')


#---------------------
#function definitions
#---------------------

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

#splits up date string
def imageDateStr(dateStr):
	strHolder = ''
	data = dateStr.split(' ')
	date = strHolder.join(data[0])
	time = strHolder.join(data[1])
	date = date.split(':')
	time = time.split(':')
	dateTimeData = [date, time]

	return dateTimeData

#input date parsing for range
def inputDateStr(dateStr1, dateStr2):
	start_date = dateStr1.split(':')
	end_date = dateStr2.split(':')
	dateRange = [start_date, end_date]
	return dateRange

#compares the dates to see if image date is in user range
def compareDates(rangeDate, imageDate):
	isInRange = False
	for n in range(0, 3, 1):
		if int(rangeDate[0][n]) <= int(imageDate[0][n]) and int(rangeDate[1][n]) >= int(imageDate[0][n]):
			isInRange = True
			break
	return isInRange


#---------------
#code execution
#---------------
rangeDate = inputDateStr(start_month, end_month)
count = 0
#goes through director
for file in os.listdir(current_directory):
	tempFile = file
	fileName, fileExt = os.path.splitext(tempFile)

	#happens if file extension is correct
	if checkExt(fileExt):
		im = Image.open(file).getexif()[36867]

		imageDate = imageDateStr(im)

		#changes name if within range of date
		if compareDates(rangeDate, imageDate):
			newName = '{}_{}{}'.format(file_name, count, fileExt)
			os.rename(file, newName)
			count += 1




