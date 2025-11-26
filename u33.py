n = str(input("Enter an integer : "))

index = len(n) - 3

while index > 0 :
	n = n[:index] + "." + n[index:]
	index -= 4

print(n)
