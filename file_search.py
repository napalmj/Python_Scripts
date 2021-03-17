#! /usr/bin/python
'''
Author: Nathaniel
-------------------------------------------------------------------------------
Python version: 3.8.5
Script Usage: scans directory for matching files. Input string via command line
-------------------------------------------------------------------------------

'''

import os
import sys


curr_dir = os.getcwd()
string_input = sys.argv[1]

#compares string lengths
def compare_len(str_in, str_dir):
	flag = True
	if str_in > str_dir:
		flag = False
	return flag

#checks user string versus director string files
def file_check(str_in, str_dir):
	flag = False
	str_len = len(str_in)
	str_dir_len = len(str_dir)
	string_in = list(str_in)
	string_dir = list(str_dir)

	
	for i in range(0, str_len, 1):
		if string_in[i] == string_dir[i] and compare_len(str_len, str_dir_len):
			flag = True

		else:
			flag = False
			break

	return flag

#scans directory for all files listed
def dir_scan():
	for file in os.listdir(curr_dir):
		if file_check(string_input, file):
			print(file)


#calls dir_scan to start script
dir_scan()

