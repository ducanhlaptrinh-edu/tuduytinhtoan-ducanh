n = list(map(str,input().split()))
k = int(input())
dic = {}
i = 0 
j = 0	
running = True
while running : 
	j = i + 1 
	if j < len(n) and int(n[j]) > k : 
		dic[n[i]] = n[j]
	elif j >= len(n) : 
		running = False
	i += 2
print(dic)