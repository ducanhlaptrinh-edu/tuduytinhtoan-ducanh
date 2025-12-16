n = tuple(map(int,input().split()))

even_nums = []
odd_nums = []
for i in range(len(n)) : 
	if i == 0 or i%2 == 0 : 
		even_nums.append(i) 
	else : 
		odd_nums.append(i)
print(tuple(even_nums))
print(tuple(odd_nums))