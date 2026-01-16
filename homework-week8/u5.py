import sys
def solve() : 
	input_data =  sys.stdin.readlines()
	if not input_data : 
		return

	iterator = iter(input_data) 

	def check(i , j , list1 , list2) : 

		if i == len(list1) : 
			return j <= len(list2)
		first_num = list1[i] 


		if j < len(list2) : 
			if first_num == list2[j] : 
				return check(i+1 , j+1 , list1 , list2)
			else :
				i = 0  
				return check(i , j+1 , list1 , list2)

	for _ in range(2) : 
		try  :
			list1 = list(map(int, next(iterator).split()))
			list2 = list(map(int, next(iterator).split()))
			
			if check(0 , 0 , list1 , list2) : 
				print("Yes")
			else : print("No")
		except StopIteration : 
			break

if __name__ == "__main__" : 
	solve()

#--------------------------------------------#
#list slicing#

def solve() : 
	input_data = sys.stdin.readlines()
	if not input_data : 
		return

	iterator = iter(input_data)

	list1 = list(map(int , next(iterator).split()))
	list2 = list(map(int , next(iterator).split()))

	if checksubarray(list1 , list2) : 
		print("YES")
	else : 
		print("NO")

	def checksubarray(list1 , list2) : 
		n = len(list1)
		m = len(list2)

		if n > m : 
			return False

		for k in range(m-n+1) : 
			sub_segment = list2[k : k+n]
			if list1 == sub_segment :
				return True
		return False

if __name__ == '__main__':
	solve()