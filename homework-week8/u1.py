def merged_two_sorted_list(list1 , list2) : 
	i = 0
	j = 0 
	n1 = len(list1)
	n2 = len(list2)

	list_merged = []

	while i < n1 and j < n2 : 
		if list1[i] < list2[j] : 
			list_merged.append(list1[i])
			i+=1
		elif list1[i] > list2[j] : 
			list_merged.append(list2[j])
			j += 1 
		else : 
			list_merged.append(list1[i])
			list_merged.append(list2[j])
			i+=1 
			j+=1
	if i < n1 : 
		list_merged.extend(list1[i:])
	if j < n2 : 
		list_merged.extend(list2[j:])

	return list_merged

if __name__ == "__main__" : 
	list1 = input().split()
	list2 = input().split()

	print(merged_two_sorted_list(list1,list2))

