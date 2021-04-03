'''
Name: Nathaniel

Ran with: Python 3
'''
#combines alternating chars of 2 strings
def newString(a, b):
    str1 = []
    str2 = []
    strFinalList = []
    fillSpace = ''
    #split up strings to list by append
    for i in a:
        str1.append(i)
    for i in b:
        str2.append(i)
    
    lenStr1 = len(str1)
    lenStr2 = len(str2)
    j = 0
    #mix and convert to final list
    while lenStr1 > 0 or lenStr2 > 0:
        if(0 < lenStr1):
            strFinalList.append(str1[j])
        if(0 < lenStr2):
            strFinalList.append(str2[j])
        j += 1
        lenStr1 -= 1
        lenStr2 -= 1
            
    mergedString = fillSpace.join(strFinalList)
    
    return mergedString


string1 = 'Believe'
string2 = 'Always'

print('The new string:', newString(string1, string2))




