arr = list(map(int,input().split()))
def bubble_sort(arr) : 
	for i in range(len(arr)) : 
		running = False 
		for j in range(len(arr) - i - 1) : 
			if arr[j] > arr[j+1] : 
				arr[j] , arr[j+1] = arr[j+1] , arr[j]
				running = True
		if not running : 
			break
	return arr

# print(bubble_sort(arr))

def selection_sort(arr) : 
	for i in range(len(arr)) : 
		for j in range(len(arr) -1 ) :
			if arr[j] > arr[j+1] : 
				arr[j] , arr[j+1] = arr[j+1] , arr[j]
	return arr 

print(selection_sort(arr))


