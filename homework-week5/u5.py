n = list(map(int,input().split()))

# key = [positives , negatives , zeros]

dic = {}
for x in n : 
	if x == 0 : 
		if "zeros" not in dic : 
			dic["zeros"] = 1 
		else : 
			dic["zeros"] += 1 
	if x > 0 : 
		if "positives" not in dic : 
			dic["positives"] = 1 
		else : 
			dic["positives"] += 1 
	if x < 0 : 
		if "negatives" not in dic : 
			dic["negatives"] = 1 
		else : 
			dic["negatives"] += 1 
print(dic)