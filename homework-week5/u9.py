dic_1 = {
}

dic_2 = {
}

dic = {}

user1 = list(map(str,input().split()))
user2 = list(map(str,input().split()))

for i in range(len(user1)) : 
	user1[i] = user1[i].split(":")
	key = user1[i][0]
	value = int(user1[i][1])
	dic_1[key] = value

for i in range(len(user2)) : 
	user2[i] = user2[i].split(":")
	key = user2[i][0]
	value = int(user2[i][1])
	dic_2[key] = value

dic = dic_1.copy()

for key , value in dic_2.items() : 
	if key in dic : 
		dic[key] += value
	else : 
		dic[key] = value 
print(dic)

