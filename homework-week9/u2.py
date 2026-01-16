try : 
	my_list = list(map(int , input().split()))
	n = len(my_list)
	print(my_list[n])
except IndexError : 
	print("List index out of range")
