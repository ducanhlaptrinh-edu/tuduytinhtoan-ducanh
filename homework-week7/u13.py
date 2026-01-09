import math
class Triangle() : 
	def __init__(self , edge1 , edge2 , edge3) : 
		self.edge1 = int(edge1)
		self.edge2 = int(edge2)
		self.edge3 = int(edge3)

	def valid_check(self) : 
		a =  self.edge1
		b =  self.edge2
		c =  self.edge3
		if a <= 0 or b <= 0 or c <= 0 or a == b or b == c or c == a or a >= (b+c) or b>=(a+c) or c>=(a+b): 
			return False 
		return True

	def cal_area(self) : 
		if self.valid_check() : 
			a = self.edge1
			b = self.edge2
			c = self.edge3
			half_circumference = (a+b+c) / 2 
			p = half_circumference
			area = round(math.sqrt(p*(p-a)*(p-b)*(p-c)),2)
			return area
		else : 
			return -1 

if __name__ == "__main__" : 
	inf = input("Enter the parameters for the three sides of a triangle (x y z) : ").split()
	triangle = Triangle(inf[0],inf[1],inf[2])

	if triangle.cal_area() != -1 : 
		print(triangle.cal_area())
	else : 
		print("Invalid")
