A = int(input("Enter a positive integer n : "))

running = True
S = 0 
n = 0

while running : 
	n += 1
	S += 1/n
	if S >= A : 
		print("n : " + str(n))
		running = False
