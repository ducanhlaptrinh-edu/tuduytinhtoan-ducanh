def sort_answers() :
	lables = ["A" , "B" , "C" , "D"]
	datas = []
	for i in range(4) : 
		content = input()
		lable = lables[i]
		datas.append([content , lable])

	datas.sort(key= lambda x : x[0])

	answers = []
	for data in datas : 
		answers.append(data[1])
	return answers

print(sort_answers())