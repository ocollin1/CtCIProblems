
def is_unique_hashing():

	string = input("Enter test string: ")

	# build hash of size length of string with null values

	checkHash = [0] * len(string)

	# loop through string hashing letters
	for letter in string:

		# if conflict, is not unique
		if checkHash[ ord(letter) % len(string) ]  == letter:	
			print (string + " doesn't contain all unique letters")
			return
		
		
		checkHash[ ord(letter) % len(string) ] = letter


	# else, is unique
	print (string + " contains all unique letters")
	return
	
		

def is_unique_no_structs():

	# get string
	string = input("Enter test string: ")

	# compare every 2 characters
	x = 0 
	while x < len(string)-1:
		y = x + 1
		while y < len(string):
			if string[x] == string[y]:
				print (string + " doesn't contain all unique letters")
				return False
			y=y+1

		x = x + 1

	print (string + " contains all unique letters")
	return True

is_unique_hashing()
is_unique_no_structs()