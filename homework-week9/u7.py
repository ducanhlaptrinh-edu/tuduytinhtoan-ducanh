def calc_age() : 
	try : 
		age = int(input("Enter your age : "))
		result = 2025 - age
		if age < 0 : 
			print("Invalid age.")
		else : 
			print("Your year of birth : ",result)
	except ValueError : 
		print("Invalid age.")

calc_age()