n = list(map(str,input().split()))
k = list(map(str,input().split()))

common_num = []

for i in range(len(n)) : 
	for x in k : 
		if x in n and x not in common_num : 
			common_num.append(x)
print(common_num)