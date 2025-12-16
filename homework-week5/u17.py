def set_matrix() : 
	try : 
		n = int(input("Input the dimensions of the square matrix : "))
	except ValueError : 
		print("Invalid")
		return 

	matrix = []

	print(f"Enter {n} rows ")
	for i in range(n) : 
		while True : 
			row_input = list(map(str,input().split()))
			if n == len(row_input) : 
				matrix.append(row_input)
				break
			else : 
				print("Invalid")

	print("Main diagonal elements : ")
	for i in range(n) : 
		print(matrix[i][i] , end = " ")

	print("\nSecondary diagonal elements : ")
	for i in range(n) : 
		j = n-1-i
		print(matrix[i][j] , end = " ")

set_matrix()