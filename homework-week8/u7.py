import sys
def can_place_flowers(flowerbed , k ) : 
	n = len(flowerbed)
	for i in range(n) : 
		if k <= 0 : 
			return True
		if flowerbed[i] == 0 : 
			left_empty = (i== 0) or flowerbed[i-1] == 0 
			right_empty = (i== n-1) or flowerbed[i+1] == 0 
			if left_empty and right_empty : 
				flowerbed[i] == 1 
				k -= 1 
	return k <= 0 

if __name__ == '__main__':
	data_input = sys.stdin.read().split() 
	k = int(data_input[-1])
	flowerbed = list(map(int , data_input[:-1]))
	result = can_place_flowers(flowerbed , k)
	print("True" if result else "False")
