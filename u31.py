import string

lowercase_alphabet = list(string.ascii_lowercase)
# print(lowercase_alphabet)

user = input("Enter a string of characters : ")

list_nums = []

for x in user : 
	if x.lower() not in lowercase_alphabet : 
		list_nums.append(x) 

# print(list_nums) 
total = 0
for i in range(len(list_nums)) : 
	total += int(list_nums[i])

print(total)

