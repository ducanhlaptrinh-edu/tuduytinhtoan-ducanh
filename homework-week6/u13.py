#def harmonious_num_sequence(nums) : 
# 	list_count = []
# 	for i in range(len(nums)) : 
# 		count = 0
# 		for j in range(1 , len(nums)) : 
# 			if nums[j] - nums[i] <= 1 : 
# 				count += 1 
# 		list_count.append(count)
# 	return max(list_count)
# print(harmonious_num_sequence(nums))

# ---------------------------------------------------------
def find_longest_harmonious_subsequence(nums):
	count = {}

	for x in nums : 
		count[x] = count.get(x , 0 ) + 1
	max_length = 0
	for x in count : 
		length = 0
		if x+1 in count : 
			length = count[x] + count[x+1]
			max_length = max(max_length , length)
	return max_length

nums =[7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,15,22,45,67,10,99,34,56,12,88,43,21,76,54,32,11,90,87,65,44,23,12,9,0,55,66,77,33,22,11,4,5,6,1,2,3,44,55,66,22,33,11,9,8,77,66,55,44,33,22,11,90,80,70,60,50,40,30,20,10,5,4,3,2,1,99,88,77,66,55]

print(find_longest_harmonious_subsequence(nums))