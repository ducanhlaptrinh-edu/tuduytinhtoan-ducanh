def check_valid() : 
	arr = list(map(int , input().split()))
	N = arr[0]
	n = len(arr) - 1 
	result = True
	if N != n : 
		result = False
	seen_number = set()
	sum_ele_arr = 0
	for x in arr[1:] : 
		if x not in seen_number : 
			seen_number.add(x)
			sum_ele_arr += x
		else : 
			result = False
	if result == True : 
		print(sum_ele_arr)
	else : 
		print("Invalid arr")

check_valid()		


