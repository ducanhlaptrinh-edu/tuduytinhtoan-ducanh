n = int(input())
while True : 
	arr = list(map(int , input().split()))
	if n == len(arr) : 
		break 

def find_seven_index(n , arr) : 
	list_ind = []
	for i , value in enumerate(arr) : 
		if value == 7 : 
			list_ind.append(i)
	if list_ind : 
		list_ind.reverse()
		for x in list_ind : 
			print(x , end= " ")
	else : 
		print("Not Found")

find_seven_index(n , arr)