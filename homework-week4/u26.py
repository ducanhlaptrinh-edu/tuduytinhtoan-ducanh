A = int(input("Enter a positive integer A : "))

list_nums = [1 , 1]

running = True 
s = 0
i = 0
while running :  
	s = list_nums[i] + list_nums[i+1]
	i += 1 
	list_nums.append(s)
	if s > A : 
		print(list_nums[-2])
		running = False

