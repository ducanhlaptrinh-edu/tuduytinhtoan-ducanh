n = int(input("Enter a positive integer n (n<=1000) : "))

running = True
i = 2

while running : 
	if i % 2 == 0 :
		print(i , end=" ")
	i += 1
	if i > n : 
		running = False
