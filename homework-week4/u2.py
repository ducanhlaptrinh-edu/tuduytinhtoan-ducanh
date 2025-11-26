def is_prime(n) : 
	if n < 2 : 
		return False 
	for i in range(2 , int(n**0.5) + 1) : 
		if n % i == 0 : 
			return False 
	return True

running = True
while running : 
	user = int(input("Enter a number : "))
	if user > 0 : 
		running = False

if is_prime(user) : 
	print("True")
else : 
	print("False")

