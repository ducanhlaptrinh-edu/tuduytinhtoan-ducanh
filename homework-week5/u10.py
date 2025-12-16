n = list(map(int,input().split()))
k = int(input())

num1 = []
num2 = []

for i in range(len(n)): 
	for j in range(j+1 , len(n)) : 
		if n[j] + n[i] == k : 
			if n[i] not in num1 and n[j] not in num2 : 
				num1.append(n[i])
				num2.append(n[j])

result = set()
result.append((num1 , num2))
last_re = sorted(list(result))
print(result)
print(num1)
print(num2)
