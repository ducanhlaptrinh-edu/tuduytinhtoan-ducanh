import string

lowercase_alphabet = list(string.ascii_lowercase)
numbers = [1,2,3,4,5,6,7,8,9,0]
# print(lowercase_alphabet)

user = input("Enter a string of characters : ")

list_alp_lower = []

for x in user : 
	for i in range(len(lowercase_alphabet)) :
		if x == lowercase_alphabet[i] : 
			list_alp_lower.append(x)

list_nums = []

for x in user : 
	for i in range(len(numbers)) : 
		if x == str(numbers[i]) : 
			list_nums.append(x) 

list_alp_upper = len(user) - len(list_alp_lower) - len(list_nums)

print(list_alp_upper)
print(len(list_alp_lower))
print(len(list_nums))




