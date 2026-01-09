class Cylinder() : 
	def __init__(self , radius, height) :
		self.radius = radius
		self.height = height
	def calculate_surface_area(self) : 
		pi = 3.14
		cylin_area = round(2*pi*self.radius*self.height + 2*pi*self.radius**2,2)
		return cylin_area 
	def calculate_volume(self) : 
		pi = 3.14
		cylin_volume = round(pi*self.radius**2*self.height , 2)
		return cylin_volume

if __name__ == "__main__" : 
	cylinder_info = list(map(float,input("Enter radius , volume of cylinder : ").split()))
	radius = cylinder_info[0]
	height = cylinder_info[1]

	cyl = Cylinder(radius , height) 
	print(cyl.calculate_surface_area())
	print(cyl.calculate_volume())
