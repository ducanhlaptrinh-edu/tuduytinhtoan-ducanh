import sys 
def find_min_k_th() : 
	arr = sys.stdin.read().split() 
	all_nums = [int(x) for x in arr]

	k = all_nums[-1] 

	all_nums.pop()

	if len(all_nums) > 0 : 
		all_nums.sort()
		print(all_nums[k-1]) # tìm số nhỏ thứ k của mat (sorted_arr)

if __name__ == '__main__':
	find_min_k_th()


#chạy trên ter : nhập xong input nhấn ctr+Z rồi Enter kết thúc nhập liệu
