arr = list(map(int,input().split()))
x = int(input())

def count_occurrences(arr , x) : 
	count = 0 
	for n in arr : 
		if x == n : 
			count+=1 
	return count

print(count_occurrences(arr , x))