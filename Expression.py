import sys
a = int(input())
b = int(input())
c = int(input())

a1 = (a+b)*c
a2 = (a*b)*c
a3 = (a*b)+c
a4 = a+b+c
b1 = a+(b*c)
b2 = a*(b*c)
b3 = a*(b+c)

c1 = max(a1,a2,a3,b1,b2,b3,a4)
print(c1)