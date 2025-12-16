def set_matrix() : 
	try : 
		dim = list(map(int,input("Input the dimensions of the square matrix and positive number k (n , m , k) : ").split()))
	except ValueError : 
		print("Invalid")
		return 

	n = dim[0]
	m = dim[1]
	k = dim[2]
	matrix = []

	print(f"Enter {n} rows ")
	for i in range(n) : 
		while True : 
			row_input = list(map(int,input().split()))
			if n == len(row_input) : 
				matrix.append(row_input)
				break
			else : 
				print("Invalid")

	total = 0
	for i in range(n) : 
		total += matrix[i][k-1]

	print("Total value element in column k : " + str(total))

set_matrix() 