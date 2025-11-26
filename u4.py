n = int(input("Enter an integer : "))
def found_num_o_digits(n) :
	num_of_digits = 0
	while True : 
		num_of_digits += 1
		if n/10 < 1 : 
			break
		n = n/10
	return num_of_digits

print(found_num_o_digits(n))