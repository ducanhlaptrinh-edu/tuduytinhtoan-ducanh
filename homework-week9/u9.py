def convert_to_integer() : 
	x = input()
	try :
		int_x = int(x)	
		print(int_x)
	except ValueError : 
		print("Invalid String!!!")
convert_to_integer()

