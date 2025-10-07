a = (input("Enter the string of letters 1 : ")).lower()
b = (input("Enter the string of letters 2 : ")).lower()
# print(a)
if len(a) > len(b) : 
	print("True")
elif len(a) < len(b) : 
	print("False")
else : 
	print("Equivalent length")
