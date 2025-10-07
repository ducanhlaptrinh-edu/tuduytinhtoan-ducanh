n = int(input("Enter the number of KWh of electricity consumed : "))
if 0<n<=50 : 
	s = 1500*n
	print(s1)
elif 51<n<=100 : 
	s = 1500*50 + 2000*(n-50)
	print(s2)
elif 100<n :
	s3 = 1500*50 + 2000*50 + 3000*(n-100)
	print(s3)