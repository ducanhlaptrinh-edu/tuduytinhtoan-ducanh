arr = list(map(int,input().split()))
X = int(input())

times = 0
list_nums=[]

for x in arr : 
	for k in arr : 
		if k == x : 
			continue
		else : 
			for c in range(-50 , 50) : 
				if x + k == X*c and (x,k) not in list_nums: 
					list_nums.append((x,k))
					times += 1 
print(times)
print(list_nums)