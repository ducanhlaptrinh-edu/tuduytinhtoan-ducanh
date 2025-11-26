def is_prime(n) : 
	if n < 2 : 
		return False
	for i in range(2 , n) : 
		if n % i == 0 : 
			return False
	return True

user = input("Enter integer a , b : ").strip()
a, b = map(int,user.split())
# print(a)
total = 0 
for x in range(a,b+1) : 
	if is_prime(x) : 
		total += x 
print(total)


