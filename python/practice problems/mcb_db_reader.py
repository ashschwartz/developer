#! /usr/bin/env python3

# mcb_db_reader.py - support script to read the contents of the mcb.db file

import shelve

myFile = shelve.open('mcb')
print('')
for k, v in myFile.items():
	print(k + ': ' + v)
print('')