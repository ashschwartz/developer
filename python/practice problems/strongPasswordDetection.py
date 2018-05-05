
# strongPasswordDetection.py = Checks if the user password is strong. A strong password
# is at least 8 characters long, contains both uppercase and lowercase characters, and
# has at least one digit.

import re

hasDigitRegex = re.compile(r'\d+')
hasUpperRegex = re.compile(r'[A-Z]+')
hasLowerRegex = re.compile(r'[a-z]+')

def strongPassword(password):
	print('')
	if len(password) < 8:
		print("Your password is too short!\n")
		return False
	if hasDigitRegex.search(password) == None:
		print("Your password should contain at least 1 digit.\n")
		return False
	if hasUpperRegex.search(password) == None:
		print("Your password should contain at least 1 uppercase letter.\n")
		return False
	if hasLowerRegex.search(password) == None:
		print("Your password should contain at least 1 lowercase letter.\n")
		return False
	print("CONGRATULATIONS, YOUR PASSWORD IS STRONG!\n")

userPassword = input("Enter your password: ")
strongPassword(userPassword)