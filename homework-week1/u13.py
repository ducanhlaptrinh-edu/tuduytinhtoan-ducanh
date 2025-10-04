a = int(input("Enter the positive integer a: "))
b = int(input("Enter the positive integer b: "))
total = a*b
print("product a and b : " + str(total))
unit_digit = total % 10
print("The unit digit is :" + str(unit_digit))