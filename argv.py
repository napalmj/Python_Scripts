# main.py
import sys

def spl(word):
	return [char for char in word]

first = sys.argv[1]

print(first)
print(type(first))

print(spl(first))
l1 = spl(first)
if l1[0] == 'f':
	print('its in there')

print(list(first))

l2 = list(first)

if l2[0] == 'f':
	print('its in there for l2')