A = int(input("Enter the bank deposite amount : "))
k = int(input("Enter the number of months : "))
r = 1 + 0.7*1/100
total = A*(r**k)
total = int(total)
print("Total money : " + str(total))