#! usr/bin/python3

''' 
---------------------------------------------------------------------------------------------------------------------
Version python 3.9.2
Author: Nathaniel
Script usage:
	Takes user input. 
	Outputs passwords to text file for user. 
	Randomizes characters.
---------------------------------------------------------------------------------------------------------------------
'''

import random

#list creation for extracting chars for password: they are here as options to modify the script
lowerCase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperCase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numerics = ['0','1','2','3','4','5','6','7','8','9']
specialChars = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', '<', '>', '.', '?', '/']
#all chars with less special chars
allCharsLessSpecial = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','!', '@', '#', '$', '%', '^', '*','<', '>', '?']
#is the only used char list
allChars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', '<', '>', '.', '?', '/']

pwdLen = input("Choose Password Size: ")
pwdAmount = input("Choose Password Amount: ")

#generate a password
def generate_password(charList: list, pwdSize: int):
	randCharList = random.shuffle(charList)
	newPasswdList: list = []
	newPasswdStr: str = ''
	i = 0

	while i < pwdSize:
		newPasswdList.append(random.choice(charList))
		i+=1
	newPasswdStr = newPasswdStr.join(newPasswdList)

	return newPasswdStr


def write_textfile(pwdListSize):
	pwdFile = open("password_list.txt", "w")

	i=0
	while i < pwdListSize:
		pwdFile.write(generate_password(allChars, int(pwdLen)))
		pwdFile.write('\n')
		i+=1
	pwdFile.close()

write_textfile(int(pwdAmount))