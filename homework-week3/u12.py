n = int(input("Enter the year :"))
if n % 4 == 0 and n % 100 != 0 and n % 400 != 0: 
	print("Yes")
else  :
	print("No")
