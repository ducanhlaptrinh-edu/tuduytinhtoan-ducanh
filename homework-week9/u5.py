def convert_to_integer(arr) :  
	list_int = []
	for i in range(len(arr)) :
		try :
			x = int(arr[i]) # khi arr[i] là a , x sẽ ko tính dc và sẽ chạy xuống dòng except , vì vậy x vẫn sẽ là giá trị trc đó là 4
			list_int.append(x)
		except (ValueError , TypeError)  : 
			print(f"it is not possible to convert the value of '{arr[i]}' to an integer!!! , skipped.")
	return list_int

arr = [1,3,4,"a","3"]
print(convert_to_integer(arr))