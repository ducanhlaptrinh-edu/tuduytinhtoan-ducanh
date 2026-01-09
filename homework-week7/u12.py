class Part_complex_number() : 
	def __init__(self , real , img) : 
		self.real = int(real)
		self.img = int(img)

class Complex_number() : 
	def __init__(self) : 
		self.nums = []

	def add(self , complex_n) : 
		self.nums.append(complex_n)

	def multiply(self) : 
		A = self.nums[0]
		B = self.nums[1]

		a1 = A.real
		b1 = A.img
		a2 = B.real
		b2= B.img

		new_real = a1*a2-b1*b2
		new_img = a1*b2 + a2*b1

		return new_real , new_img

if __name__ == "__main__" : 
	complex_num = Complex_number()
	print("Enter the real and imaginary parts of the two numbers A and B, respectively :" )
	for _ in range(2) : 
		inf = input().split()
		real = inf[0]
		img = inf[1]
		complex_n = Part_complex_number(real , img)
		complex_num.add(complex_n)

	new_real , new_img = complex_num.multiply()
	print(str(new_real) + " " + str(new_img))
