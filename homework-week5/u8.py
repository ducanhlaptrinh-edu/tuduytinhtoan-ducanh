n = list(map(str,input().split()))

dic = {}

for x in n : 
	if x not in dic : 
		dic[x] = 1 
	else : 
		dic[x] += 1 
print(dic)

