n = int(input())
while True : 
	arr = list(map(str , input().split()))
	if n == len(arr) : 
		break 

def find_people(n , arr) : 
	index_name = []
	for i , name in enumerate(arr) : 
		if name == "Nemo" : 
			if i == 0 :
				index_name.append(1)
				index_name.append(n-1)
			elif i == n-1 : 
				index_name.append(0)
				index_name.append(n-2)
			else : 
				index_name.append(i-1)
				index_name.append(i+1)

	for k in index_name : 
		print(arr[k])

find_people(n,arr)