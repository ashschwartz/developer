testList = ['apples', 'bananas', 'tofu', 'cats', 'monkeys', 'pans']

def printList(someList):
    for i in range(len(someList)):
    	if i < len(someList) - 1:
    		print(someList[i] + ', ', end='')
    	else:
    		print('and ' + someList[i] + '.')

printList(testList)