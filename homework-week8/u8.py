def is_path_crossing(moves) : 
	x , y = 0 , 0 
	result = {(0,0)}

	cmd = list(moves) 
	for l in cmd : 
		if l == "U" : 
			y += 1
		if l == "D" : 
			y -= 1
		if l == "R" : 
			x += 1
		if l == "L" : 
			x -= 1

		pos = (x,y)
		if pos in result : 
			return True
		result.add(pos)
	return False

if __name__ == '__main__':
	moves = input() 
	if is_path_crossing(moves) :
		print("True")
	else : 
		print("False")
