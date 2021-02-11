'''
----------------------------------------------------------------------------------------------
 Script Usage: Renames all extensions specified by the user to the extension the user chooses
 How to use: script run via command line. first arg is current ext, second arg is final ext.
 Version: python 3.8.7
----------------------------------------------------------------------------------------------
'''

#!/usr/bin/env python3
import os
import sys

#checks for correct user input
def check_dot(ext):
	temp = list(ext)
	if temp[0] != '.':
		print('Extensions must begin with a Dot --> .\n')
		print('Nothing implimented.\nExiting...')
		exit()

ext_current = sys.argv[1]
ext_final = sys.argv[2]

#call function
check_dot(ext_current)
check_dot(ext_final)

#gets current directory
current_dir = os.getcwd()

for file in os.listdir(current_dir): #listdir
	fileName, fileExt = os.path.splitext(file) #splitting file text
	if fileExt == ext_current: #seperate all file extensions with cxx
		fileExt = ext_final #overwrite to cpp
	newExt = '{}{}'.format(fileName,fileExt) #resetting format
	os.rename(file, newExt) #resetting to directory with rename
