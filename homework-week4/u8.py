n = int(input("Enter a positive integer : "))
steps = 0
running = True
while running : 
	n = n + int(''.join(reversed(str(n))))
	steps += 1

#doi bien n thanh s de quay lai vong lap n khong phai la string
	s = str(n)
	length = len(s)
	is_palin = True

	for i in range(int(length/2)) : 
		if s[i] != s[length - i - 1] : 
			is_palin = False
			break
	if is_palin : 
		running = False

print(steps , n)



