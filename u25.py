list_nums = []

running = True 
while running:
	n = int(input("Enter a positive integer n : "))
	if n != -1 : 
		list_nums.append(n)
		continue
	else : 
		running = False
print(list_nums)
print("Max number in list : " + str(max(list_nums)))
print("Min number in list : " + str(min(list_nums)))




	
