#! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#		 py.exe mcb.pyw delete <keyword> - Deletes entry from file.
#		 py.exe mcb.pyw delete ALL - Deletes all entries from file.
#		 py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#		 py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content or delete it.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
	print('SAVE')
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	if sys.argv[2] == 'ALL':
		for i in mcbShelf.keys():
			del mcbShelf[i]
		print('BURN IT DOWN')
	elif sys.argv[2] in mcbShelf:
		del mcbShelf[sys.argv[2]]
		print('Deleted ' + sys.argv[2] + ' from file.')
	else:
		print('No key matching ' + sys.argv[2] + '.')
elif len(sys.argv) == 2:
	# List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
		print('LIST')
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
		print('COPY')

mcbShelf.close()