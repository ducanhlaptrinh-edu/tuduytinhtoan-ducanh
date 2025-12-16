user = list(map(str,input().split()))

dic = {}

for i in range(len(user)) : 
	user[i] = user[i].split(":")
	if user[i][0] not in dic : 
		dic[user[i][0]] = [user[i][1]]
	else :
		dic[user[i][0]].append(user[i][1])


print(dic)