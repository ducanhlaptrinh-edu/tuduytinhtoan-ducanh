def is_isomorphic(word_a , word_b) : 
	if len(word_a) != len(word_b) : 
		return False

	map_a_to_b = {}
	map_b_to_a = {}

	for char_a , char_b in zip(word_a,word_b) : 
		if char_a in map_a_to_b : 
			if map_a_to_b[char_a] != char_b : 
				return False
		else : 
			map_a_to_b[char_a] = char_b

		if char_b in map_b_to_a : 
			if map_b_to_a[char_b] != char_a : 
				return False
		else : 
			map_b_to_a[char_b] = char_a

	return True

if is_isomorphic("abab" , "cscd") : 
	print("True")
else : 
	print("False")