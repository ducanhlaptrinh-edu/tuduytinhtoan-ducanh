user = input("Enter numbers separated by commas :  ")

list_nums = list(map(int , user.strip().split(", ")))
# print(list_nums)

total = 0

for i in range(len(list_nums)) : 
	total += int(list_nums[i])

print(total)