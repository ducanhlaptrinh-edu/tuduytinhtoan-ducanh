n = 99
list_nums = []
for i in range(1 , 99) :
	if i%3 == 0 and i%2 == 0 : 
		list_nums.append(i)

for x in list_nums : 
	print(str(x) + " " , end="")
