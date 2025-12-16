n = list(map(int,input().split()))

def common_element(n) : 
	index = {}
	for x in n : 
		if x in index : 
			index[x] += 1 
		else : 
			index[x] = 1 

	last_num = n[0]
	max_index = 0 

	for x in index : 
		times = index[x]
		if times > max_index : 
			max_index = times 
			last_num = x
		elif times == max_index : 
			if x < last_num :
				last_num = x
	return last_num

print(common_element(n))


