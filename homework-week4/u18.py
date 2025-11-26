a = int(input("Enter a positive integer a : "))
b = int(input("Enter a positive integer b : "))

numbers1 = []
for i in range(1 , a+1) :
	if a % i == 0 : 
		numbers1.append(i)

numbers2 = []
for j in range(1 , b+1) :
	if b % j == 0 : 
		numbers2.append(j)

similars = []

for x in numbers1 : 
	for w in numbers2 :
		if x == w :
			similars.append(w) 

for z in similars : 
	print(str(z) + " " , end="")
