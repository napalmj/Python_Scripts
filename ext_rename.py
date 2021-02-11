'''
----------------------------------------------------------------------------------------------
 Script Usage: Renames all extensions specified by the user to the extension the user chooses
 Version: python 3.8.7
----------------------------------------------------------------------------------------------
'''

#!/usr/bin/env python3
import os

#gets current directory
current_dir = os.getcwd()

#takes user input 
userExtOriginal = input("Original extension name to be reassigned: ")
userExtFinal = input("Final extension name to be assigned: ")

for file in os.listdir(current_dir): #listdir
	fileName, fileExt = os.path.splitext(file) #splitting file text
	if fileExt == userExtOriginal: #seperate all file extensions with cxx
		fileExt = userExtFinal #overwrite to cpp
	newExt = '{}{}'.format(fileName,fileExt) #resetting format
	os.rename(file, newExt) #resetting to directory with rename
