n = int(input("Enter a positive integer : ").strip())
user = list(map(int , input("Enter " + str(n) + " integer : ").strip().split()))
# print(user)
found = False 
for x in user : 
	if x == 42 : 
		found = True
if found : 
	print("I've found the meaning of life!")
else : 
	print("It's a joke!")


