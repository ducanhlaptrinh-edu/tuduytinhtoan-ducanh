a,b,c = map(float , input("Enter three edge of triangle : ").split())
if (a+b)>c or (a+c)>b or (b+c)>a and a>0 and b>0 and c>0 : 
	p = (a+b+c)/2
	acreage = (p*(p-a)*(p-b)*(p-c))**0.5
	print("Acreage of triangle is : " + str(acreage))
else : 
	print("Three edge is not of triangle!!!")