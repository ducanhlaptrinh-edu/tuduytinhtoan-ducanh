try : 
	a = int(input("Enter an positive integer a : "))
	b = int(input("Enter an positive integer b : "))
	result = a + b 
except ZeroDivisionError : 
	print("Error : Cannot be divided by zero.")
except ValueError : 
	print("Error : Please enter positive integer. ")
except Exception as e : 
	print("Error !!!")
else : 
	print("Result a + b :", str(result))
finally : 
	print("Finished.")