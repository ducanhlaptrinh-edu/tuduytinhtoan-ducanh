user = input("Enter a character: ")
new_user = ord(user)
if new_user>=65 and new_user<=90 or new_user>=97 and new_user<=122 : 
	print(user + " is alphabet")
else : 
	print(user + " is not alphabet")