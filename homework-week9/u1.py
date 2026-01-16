try : 
	a = int(input())
	b = int(input())
	result = round(a/b,2)
	print(result)
except ZeroDivisionError : 
	print("Cannot be divided by zero")
