#! /usr/bin/python

''' 
---------------------------------------------------------------------------------------------------------------------
Version python 3.9.2
Author: Nathaniel
Script usage:
	this is intended for renaming large groups of photos
	run script -> python by_date_rename.py 'date range by noting as: YEAR-MM-DD YEAR-MM-DD' 'new_name (no extension)'
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

#goes through director
for file in os.listdir(current_directory):
	tempFile = file
	fileName, fileExt = os.path.splitext(tempFile)

	if checkExt(fileExt):
		print(file)

