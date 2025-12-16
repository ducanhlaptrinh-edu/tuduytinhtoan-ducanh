n = list(map(int,input().split()))

list_num = []
for i in range(len(n)) : 
	if n[i] not in list_num : 
		list_num.append(n[i])

print(list_num)
