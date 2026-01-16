import math
def calc_sqrt() : 
	try : 
		x = int(input("Enter a positive integer : "))
		result = round(math.sqrt(x),2)
	except ValueError : 
		print("Negative number")
	else : 
		print("Result : ",result)

calc_sqrt()