n = float(input("Enter the number : "))
if n >= 0 : 
	round_down = int(n)
else : 
	if n == int(n) : 
		round_down = int(n)
	else : 
		round_down = int(n) -1 

if n >= 0 : 
	if n == int(n) :
		round_up = n
	else : 
		round_up = int(n) + 1
else : 
	round_up = int(n)

if n - int(n) >= 0.5 : 
	round_nearest = int(n) + 1
elif n - int(n) <= -0.5 : 
	round_nearest = int(n) - 1
else :
	round_nearest = int(n)

print(str(round_up) + " " + str(round_down) + " " + str(round_nearest))
