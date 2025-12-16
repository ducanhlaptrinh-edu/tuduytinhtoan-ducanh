n = tuple(map(int,input().split()))
k = int(input())

last_dance = len(n) - k 

new_list = []
for i in range(last_dance) : 
	new_list.append(n[k+i])

for j in range(k) : 
	new_list.append(n[j])
	
print(tuple(new_list))


