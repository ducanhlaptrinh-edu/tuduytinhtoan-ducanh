def binary_search(arr , left , right , target) : 
	if left > right : 
		return
	mid = left + (right - left) // 2 
	if arr[mid] == target : 
		return mid 
	elif arr[mid] < target : 
		return binary_search(arr , mid + 1  , right , target)
	else : 
		return binary_search(arr , left , mid - 1, target)
	return -1 
arr = list(map(int,input().split()))
target = int(input())
left = 0
right = len(arr) - 1
print(binary_search(arr , left , right , target	))