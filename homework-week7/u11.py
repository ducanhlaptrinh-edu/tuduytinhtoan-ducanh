import math
class Coordinates() : 
	def __init__(self ,x ,y ,z) : 
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)
		
class Point() : 
	def __init__(self) : 
		self.points = []

	def add(self , coordinate) : 
		self.points.append(coordinate)

	def vector(self) : 
		A = self.points[0]
		B = self.points[1]
		C = self.points[2]
		D = self.points[3]
		n1 = ((B.y-A.y)*(C.z-A.z)-(C.y-A.y)*(B.z-A.z),(B.z-A.z)*(C.x-A.x)-(C.z-A.z)*(B.x-A.x),(B.x-A.x)*(C.y-A.y)-(C.x-A.x)*(B.y-A.y))
		n2 = ((B.y-C.y)*(D.z-B.z)-(D.y-B.y)*(B.z-C.z),(B.z-C.z)*(D.x-B.x)-(D.z-B.z)*(B.x-C.x),(B.x-C.x)*(D.y-B.y)-(D.x-B.x)*(B.y-C.y))
		return n1 , n2

	def find_angle(self) : 
		n1, n2 = self.vector()
		tvh = abs(n1[0]*n2[0] + n1[1]*n2[1] + n1[2]*n2[2])
		tdd = math.sqrt(n1[0]**2 + n1[1]**2 + n1[2]**2)*math.sqrt(n2[0]**2 + n2[1]**2 + n2[2]**2)
		cos_a = tvh/tdd
		rad = math.acos(cos_a)
		degree = round(math.degrees(rad),2)
		return degree

if __name__ == "__main__" : 
	point = Point()
	print("Input 4 points on the Oxyz coordinate system (A,B,C,D) : ")
	for _ in range(4) : 
		info = input().split()
		x = info[0]
		y = info[1]
		z = info[2]
		coordinate = Coordinates(x,y,z)
		point.add(coordinate)
	print(point.find_angle())




