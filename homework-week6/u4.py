arr = list(map(int,input().split()))

def find_num(arr) : 
	dic = {}
	for x in arr :
		if x not in dic : 
			dic[x] = 1
		else : 
			dic[x] += 1

	last_num = None
	max_val = 0 
	for key , value in dic.items() : 
		if value > max_val : 
			max_val = value
			last_num = key
	return f"{last_num} appear most frequently and earliest"

print(find_num(arr))

