#! /usr/bin/python

''' 
---------------------------------------------------------------------------------------------------------------------
Version python 3.9.2
Script usage:
	lists all dates of files in directory
---------------------------------------------------------------------------------------------------------------------
'''


import os.path
import time

#establishing current directory
current_directory = os.getcwd()

for file in os.listdir(current_directory):
	#creationTimeEpoch = os.path.getctime(file)
	#creationTime = time.strftime('%Y-%m-%d', time.localtime(creationTimeEpoch))
	#fileStat = os.stat(file)
	#creationTime = time.ctime(fileStat [stat.ST_CTIME])
	#print(file, creationTime)
	modDate = time.ctime(os.path.getmtime(file)) #gets string of last modified date
	print(modDate)
