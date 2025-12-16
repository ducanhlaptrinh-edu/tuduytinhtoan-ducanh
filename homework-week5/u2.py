n = list(map(int,input().split()))

list_num = [n[0]]

for i in range(1, len(n)) : 
	total = 0
	for j in range(i+1) : 
		total += n[j]
	list_num.append(total)

print(list_num)
