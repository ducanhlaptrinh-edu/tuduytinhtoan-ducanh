class Rectangle() : 
	def __init__(self , w , h , k) : 
		self.w = w 
		self.h = h 
		self.k = k 

	def scale(self) : 
		self.w = self.w * self.k
		self.h = self.h * self.k

	def area(self) : 
		area = self.w * self.h
		return area

	def perimeter(self) : 
		perimeter = (self.w + self.h) * 2 
		return perimeter


if __name__ == "__main__" : 
	user = input("Enter the rectangle dimension and coefficient (w,h,k) : ")
	dimesion = user.split(",")
	w = int(dimesion[0])
	h = int(dimesion[1])
	k = int(dimesion[2])

	rectangle = Rectangle(w,h,k)
	rectangle.scale()

	print(str(rectangle.area()) + " " + str(rectangle.perimeter()))
