a = int(input("Enter the positive integer a :"))
b = int(input("Enter the positive integer b :"))
c = int(input("Enter the positive integer c :"))
if ( a < b+c and b < a+c and c < a+b ) and a>0 and b>0 and c>0 : 
	print("Yes")
else : 
	print("No")