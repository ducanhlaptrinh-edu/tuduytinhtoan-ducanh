a = str(input())
b = str(input())

a = a.split(" ")
b = b.split(" ")

list_char = []

for x in a : 
	if x not in b : 
		list_char.append(x)

for i in range(len(list_char)) : 
	print(list_char[i] , end=" ")





