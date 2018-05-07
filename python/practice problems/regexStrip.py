#! /usr/bin/env python3

# regexStrip.py = takes an argument and strips that character from a string the user specifies.
# If no argument, then whitespace characters will be removed from the beginning and end of the string.

import sys, re

try:
	text = sys.argv[1]
	validArguments = True
	try:
		subCharacters = sys.argv[2]
	except:
		subCharacters = ' '
except:
	print("You must enter a text string as an argument")
	exit()

def characterRemoval(localText):
	for i in subCharacters:
		subRegex = re.compile((i), re.IGNORECASE)
		localText = subRegex.sub('', localText)
	return localText

newText = characterRemoval(text)
print(newText)