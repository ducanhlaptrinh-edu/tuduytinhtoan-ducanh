import time
n = int(input("Enter a positive integer : "))
start = time.time()
list_nums = []
for i in range(1 , n + 1) : 
	if i % (i**0.5) == 0 : 
		list_nums.append(i)

for x in list_nums : 
	print(str(x) + " " , end="")
end = time.time()
print(end-start)
