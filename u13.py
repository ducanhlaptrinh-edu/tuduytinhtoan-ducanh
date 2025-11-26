a = int(input("Enter a positive integer a : "))
b = int(input("Enter a positive integer b : "))

numbers1 = []
for i in range(1 , a ) :
	if a % i == 0 : 
		numbers1.append(i)

numbers2 = []
for j in range(1 , b ) :
	if b % j == 0 : 
		numbers2.append(j)

# print(numbers1)
# print(numbers2)

total_1 = 0
total_2 = 0

for x1 in numbers1 : 
	total_1 += x1

for x2 in numbers2 : 
	total_2 += x2

# print(total_1)
# print(total_2)

if a == total_2 and b == total_1 : 
	print("true")
else : 
	print("false")



