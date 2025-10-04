scores = input().split()
a1,b1,c1,a2,b2,a3 = map(float , scores)
average = ((a1+b1+c1) + (a2+b2)*2 + a3*3)/10
print("Average point =  " + str(average))