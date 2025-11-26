running = True
while running : 
	n = float(input("Enter a integer (1-99) :  "))
	if 1 < n and n < 100 and n % int(n) == 0 : 
		running = False
result = 1 
for i in range(1 , int(n)+1) : 
	result *= i 
print(result)

