import string

lowercase_alphabet = list(string.ascii_lowercase)
# print(lowercase_alphabet)

user = input("Enter a string of characters : ")

list_alp = []

for x in user : 
	for i in range(len(lowercase_alphabet)) : 
		if x.lower() == lowercase_alphabet[i] : 
			list_alp.append(x)

print(list_alp[0]) 
# print(list_alp) 


