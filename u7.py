n = int(input("Enter a positive integer n (n>=2) : "))
numbers = []
for i in range(2 , n+1 ) :
	if n % i == 0 : 
		numbers.append(i)

def is_prime(x) : 
	if x < 2 : 
		return False
	for i in range(2 , x) : 
		if x % i == 0 : 
			return False
	return True

primes = []
for k in numbers : 
	if is_prime(k) : 
		primes.append(k)

print(max(primes))



