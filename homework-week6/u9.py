# arr = list(map(int,input().split()))

# list_res = []

# for i in range(len(arr)) : 
# 	count = 0
# 	for j in range(i , len(arr)) : 
# 		if arr[i] > arr[j] : 
# 			count += 1 
# 	list_res.append(count)
# print(list_res)

import bisect #(Binary search)sắp xếp tăng dần , nhảy vào giữa so sánh , giảm độ phức tạp

def count_smaller_bisect(nums):
	sorted_seen = []

	count = []

	for num in nums.reverse() : 
		index = bisect.bisect_left(sorted_seen , num)

		count.append(index)

		bisect.insort(sorted_seen , num) # bs.insort luôn thêm value : num vào danh sách theo thứ tự tăng dần 
										 # còn list.insert(index , value) : chủ động mình muốn

	return count.reverse()