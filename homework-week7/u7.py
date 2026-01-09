import math
class Fraction() : 
	def __init__(self , num , den) : 
		if den == 0 : 
			raise ValueError("The denominator must be different from 0 !!")
		if den < 0 : 
			num = -num
			den = -den

		common_convention = math.gcd(num , den)
		self.num = num // common_convention 
		self.den = den // common_convention

	def add(self , other) :
		new_num = self.num*other.den + other.num*self.den
		new_den = self.den*other.den
		return Fraction(new_num , new_den)

	def sub(self, other) : 
		new_num = self.num*other.den - other.num*self.den
		new_den = self.den*other.den
		return Fraction(new_num , new_den)

	def mul(self , other) : 
		new_num = self.num*other.num
		new_den = self.den*other.den
		return Fraction(new_num , new_den)

	def div(self , other) : 
		new_num = self.num*other.den 
		new_den = self.den*other.num
		return Fraction(new_num , new_den)

	def __str__(self) : 
		return f"{self.num}/{self.den}"

def menu_display() : 
	try : 
		user_input = input()
		element = user_input.split()
		if len(element) != 5 : 
			print("Invalid")
			return	

		num_1 = int(element[0])
		den_1 = int(element[1])
		op = element[2]
		num_2 = int(element[3])
		den_2 = int(element[4])

		f1 = Fraction(num_1,den_1)
		f2 = Fraction(num_2,den_2)

		result = None

		if op == "+" : 
			result = f1.add(f2)
		if op == "-" : 
			result = f1.sub(f2)
		if op == "*" : 
			result = f1.mul(f2) 
		if op == "/" : 
			result = f1.div(f2)

		if result : 
			print(result)
		else : 
			print("Invalid")
	except : 
		print("Invalid ")

if __name__ == "__main__" : 
	menu_display()
