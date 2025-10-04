a = int(input("Enter a length of rectangle : "))
b = int(input("Enter a width of rectangle : "))
s1 = a*b
s2 = 3.14*((b/2)**2)
ds = round(s1-s2,2)
print("Acreage of rectangle : " + str(s1))
print("Acreage of circle : " + str(s2))
print("The rest of rectangle to grow tree : " + str(ds))



