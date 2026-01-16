def switch_2_slot() : 
	arr = list(input().strip())
	n = len(arr) 

	target = 0	
	last_idx = -1

	for i in range(n - 1) :
		suffix = arr[i+1:]
		min_val = min(suffix) 
		if min_val < arr[i] : # 12422
			for j in range(n-1 , i , -1) : 
				if arr[j] == min_val : 
					last_idx = j
					break
		arr[i] , arr[last_idx] = arr[last_idx] , arr[i]
		print("".join(arr)) # "ki tu giua 2 ele".join(list)
		return
	arr[-1] , arr[-2] = arr[-2] , arr[-1]
	print("".join(arr))
	
if __name__ == '__main__':
	switch_2_slot()