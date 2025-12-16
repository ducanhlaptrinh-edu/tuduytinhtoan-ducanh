n = tuple(map(str,input().split()))
print(n[0] +" "+ n[-1] , end=" ")

n = list(n)

n = ''.join(reversed(n))

print(tuple(n))
		