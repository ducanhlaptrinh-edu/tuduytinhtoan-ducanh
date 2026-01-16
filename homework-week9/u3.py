def check_happy_num() : 
	try : 
		n = int(input())

		if n <= 0 : 
			print("Please enter a positive integer")

		seen_numbers = set()

		while n != 1 and n not in seen_numbers : 
			seen_numbers.add(n)
			current_sum = 0 
			for x in str(n) : 
				current_sum += int(x)**2
			n = current_sum
		if n == 1 : 
			print("YES")
		else : 
			print("NO")
	except ValueError : 
		print("Error : Please enter a positive integer .")

if __name__ == '__main__':
	check_happy_num()