#phep toan XOR bitwise : 
a = int(input("a = "))
b = int(input("b = "))

a = a^b
b = b^a
a = a^b

print("a = " , a)
print("b = " , b)
