import math	

class Coordinates() : 
	def __init__(self , x, y) : 
		self.x = x 
		self.y = y

	def is_coordinate_origin(self) :
		if self.x== 0 and self.y== 0 :
			return True
		return False 
	def is_lies_on_the_vertical_axis(self) : 
		if self.x== 0 and self.y != 0 : 
			return True
		return False
	def is_lies_on_the_horizontal_axis(self) : 
		if self.x != 0 and self.y== 0 : 
			return True 
		return False
	def distance_to_coordinate_origin(self) : 
		distance = math.sqrt(self.x**2 + self.y**2)
		return distance

if __name__ == "__main__" : 
	user = input("Enter the coordinates : x,y : ")
	coordinate = user.split(",") 
	x = int(coordinate[0])
	y = int(coordinate[1])

	M = Coordinates(x , y) 

	if M.is_coordinate_origin() : 
		print("Point M is the origin of the coordinate system.")
	elif M.is_lies_on_the_vertical_axis() : 
		print("Point M is lies on the vertical axis.")
	elif M.is_lies_on_the_horizontal_axis() : 
		print("Point M is lies on the horizontal axis.")
	else : 
		print("Point M does not lie on the axis.")
	print("Distance from point M to origin : " + str(M.distance_to_coordinate_origin()))
