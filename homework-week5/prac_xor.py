def harming_distance(x , y) : 
	xor_result = x ^ y
	xor_result = bin(xor_result) #bin() chuyển thành dãy số nhị phân
	print(xor_result)
	count = 0
	for x in xor_result : 
		if x == "1" : 
			count += 1
	return count
print(harming_distance(1, 4))