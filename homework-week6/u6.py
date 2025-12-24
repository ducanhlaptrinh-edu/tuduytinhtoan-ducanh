arr = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flat_arr = []

for i in range(len(arr)) : 
	for j in range(len(arr[i])) : 
		flat_arr.append(arr[i][j])

print(flat_arr)
