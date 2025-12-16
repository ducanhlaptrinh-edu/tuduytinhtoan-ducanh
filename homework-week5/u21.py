n = list(map(str,input().split()))

dic = {}

for index , elements in enumerate(n) : 
	if elements in dic : 
		dic[elements].append(index)
	else : 
		dic[elements] = [index] # lí do có ngoặc vuông : mình cần khởi tạo một list gồm index của element để có thể thêm vào 

print(dic)