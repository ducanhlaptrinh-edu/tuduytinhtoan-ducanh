n = int(input("Enter a positive integer n : "))

running = True
S = 0 
k = 0

while running : 
	k += 1
	S += k
	if S >= n : 
		print("k : " + str(k))
		running = False
