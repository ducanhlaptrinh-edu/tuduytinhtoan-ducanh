import sys
def solve(arr) : 
	n = len(arr) 
	i = n - 2 
	while arr[i] >= arr[i+1] and i>=0 : 
		i-=1
	if i == -1 : 
		return arr.reverse()

	j = n -1 
	while arr[j] < arr[i] : 
		j-=1

	arr[i] , arr[j] = arr[j] , arr[i]

	left = i +1 
	right = n - 1 
	while left < right : 
		arr[left] , arr[right] = arr[right] , arr[left]
		left += 1 
		right -= 1

	return arr

if __name__ == '__main__':
	input_data = sys.stdin.read().split()
	n = int(input_data[0])
	arr = list(map(int , input_data[1:]))
	# print(arr)
	if n == len(arr) : 		
		print(solve(arr))
	else : 
		print("Invalid")