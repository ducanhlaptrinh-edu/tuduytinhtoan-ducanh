n = list(map(str,input().split()))
dic = {}

i = 0 
j = 0
running = True
while running : 
	j = i + 1
	if j < len(n) : 
		dic[n[j]] = n[i]
	else : 
		running = False
	i += 2

print(dic)
