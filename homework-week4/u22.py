n = str(input("Enter a positive integer n : "))

even_nums = []
for i in range(len(n)) : 
	if int(n[i]) % 2 == 0 :
		even_nums.append(i)

odd_nums = []
for j in range(len(n)) : 
	if int(n[j]) % 2 != 0 :
		odd_nums.append(j)
print("Even number of digits : " + str(len(even_nums)))
print("Odd number of digits : " + str(len(odd_nums)))
