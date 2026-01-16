import sys
def solve() : 
	input_data =  sys.stdin.read().split()
	if not input_data : 
		return

	iterator = iter(input_data) 

	try : 
		q_str = next(iterator , None)
		if not q_str : 
			return 
		Q = int(q_str)
	except StopIteration : 
		return

	def check(i,j,A,B,memo) : 
		state = (i,j)
		if state in memo : 
			return memo[state]

		if i == len(A) : 
			return j == len(B)

		char_A = A[i]
		result = False

		if char_A.isupper() : 
			if j<len(B) and char_A == B[j] : 
				result = check(i+1 , j+1 , A , B , memo)
			else : 
				result = False

		else : 
			result = check(i+1 , j , A , B , memo) 

			if not result and char_A.upper() == B[j] : 
				result = check(i+1, j+1 , A , B , memo)

		memo[state] = result
		return result

	for _ in range(Q) : 
		try : 
			a = next(iterator)
			b = next(iterator)

			memo = {}
			if check(0 , 0 , a , b , memo) : 
				print("YES")
			else : 
				print("NO")
		except StopIteration : 
			break

if __name__ == "__main__" : 
	solve()
