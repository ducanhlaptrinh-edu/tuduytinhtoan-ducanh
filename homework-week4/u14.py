m = int(input("Enter a positive integer m : "))
n = int(input("Enter a positive integer n : "))

numbers1 = []
for i in range(1 , m+1) :
	if m % i == 0 : 
		numbers1.append(i)

numbers2 = []
for j in range(1 , n+1) :
	if n % j == 0 : 
		numbers2.append(j)

similars = []

for x in numbers1 : 
	for w in numbers2 :
		if x == w :
			similars.append(w) 
print(max(similars))

