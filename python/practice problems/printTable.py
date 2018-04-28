tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David', 'Frank'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['new']]

numberOfLists = len(tableData)
maxListLength = 0
colWidths = [0] * numberOfLists


# finds the length of the longest list
for i in range(len(tableData)):
	if len(tableData[i]) > maxListLength:
		maxListLength = len(tableData[i])

# finds the length of the longest item in the list
for i in range(numberOfLists):
	for j in range(len(tableData[i])):
		if len(tableData[i][j]) > colWidths[i]:
			colWidths[i] = len(tableData[i][j])


def printTable():
	for j in range(maxListLength):
		for i in range(numberOfLists):
			if j < len(tableData[i]):
				print((tableData[i][j]).rjust(colWidths[i]), end='  ')
			else:
				print(''.rjust(colWidths[i]), end='  ')
		print()

printTable()