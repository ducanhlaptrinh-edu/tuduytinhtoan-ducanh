n = int(input("Enter a positive integer n (n>=2 and n < 10**6) : "))
if n > 10**6 :
	n = int(input("Enter a positive integer n (n>=2 and n < 10**6) : "))

numbers = []
for i in range(2 , n+1 ) :
	if n % i == 0 : 
		numbers.append(i)

# print(numbers)

even_divisors = []
for z in numbers : 
	if z % 2 == 0 : 
		even_divisors.append(z)

print(len(even_divisors))






