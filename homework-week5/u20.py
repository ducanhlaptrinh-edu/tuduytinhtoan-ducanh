n = list(map(int,input().split()))
k = int(input())

def find_index_k(n , k) : 
	for x in n : 
		if x == k : 
			return n.index(x) + 1 
	if k not in n : 
		return -1

print(find_index_k(n,k))