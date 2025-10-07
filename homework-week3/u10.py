numbers = []

for i in range(4) : 
	n = int(input("Enter the number " + str(i+1) + " : "))
	numbers.append(n)

print("The largest number is " + str(max(numbers)))