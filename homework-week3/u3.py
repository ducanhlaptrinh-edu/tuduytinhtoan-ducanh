def is_power_of_two() :
	n = int(input("Enter the number you want to check : "))
	if n > 0 and (n & (n-1)) == 0 : 
		print(str(n) + " is power of two.")
	else : 
		print(str(n) + " is not power of two.")

is_power_of_two()
