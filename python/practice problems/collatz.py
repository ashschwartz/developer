def collatz(inputNumber):
	if inputNumber % 2 == 0:
		newNumber = inputNumber // 2
	else:
		newNumber = 3 * inputNumber + 1
	print(newNumber)
	return newNumber

validInput = False
while not validInput:
	print('Pick an integer and watch the Collatz Sequence in action')
	number = input()

	try:
		number = int(number)
		validInput = True
	except:
		print('You must enter an integer')


while number != 1:
	number = collatz(number)