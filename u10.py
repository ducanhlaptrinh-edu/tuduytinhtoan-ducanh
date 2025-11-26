n = int(input("Enter a positive integer : "))
def max_nums(n) :
	list_nums = []
	running = True
	while running : 
		if n % 2 == 0 : 
			n = n/2
			list_nums.append(n)
		elif n % 2 != 0  and n != 1: 
			n = 3*n +1
			list_nums.append(n)
		if n == 1 : 
			list_nums.append(n)
			running = False
		max_n = len(list_nums) 
	return max_n
max_in_list = []
for i in range(1 , n+1) : 
	max_l = max_nums(i)
	# print(max_l)
	max_in_list.append(max_l)
max_value = max(max_in_list)
max_index = max_in_list.index(max_value)
print(max_index + 1 , max(max_in_list))

# maxx = max_nums(n)
# print(list_nums)


