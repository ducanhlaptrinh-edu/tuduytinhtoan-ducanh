print("ax + b = 0")
a = float(input("Enter the number a :"))
b = float(input("Enter the number b :"))

if a == 0 and b != 0 : 
	print("Not exist")
elif a == b == 0 : 
	print("Countless x ")
else :
	x = -b/a 
	print(round(x,2))