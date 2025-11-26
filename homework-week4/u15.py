total = int(input("Enter the number of chickens and dogs : "))
foots = int(input("Enter the number of foots : "))

if foots/2 - total == int(foots/2 - total) and 2*total - foots/2 == int(2*total - foots/2) : 
	print(str(int(foots/2 - total)) + " " + str(int(2*total - foots/2)) , end="")
else : 
	print("invalid")



