user = input("Enter an upper alphabet : ")
try : 
	if len(user) != 1 : 
		raise ValueError("Input must be a single character")
	n_user = ord(user)
	if n_user == 65 : 
		print("None")
	elif 65 < n_user <= 90 : 
		n_user = n_user + 31
		print(chr(n_user))
	else : 
		raise ValueError("Not an uppercase letter")
except Exception as e :
	print("Errol" , e)
