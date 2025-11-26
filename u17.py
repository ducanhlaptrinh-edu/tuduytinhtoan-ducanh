a = int(input("Enter a positive integer a : "))

multiplication_table = []

for i in range(1 , 11) : 
	product = a * i 
	multiplication_table.append(str(a) + " x " + str(i) + " = " + str(product))
	
for x in multiplication_table : 
	print(x)
