import math
n, m, a, b = input().split()
n1 = int(n)
m1 = int(m)
a1 = int(a)
b1 = int(b)
n2 = n1
sum1 = 0 
n3 = n1
m3 = m1
b3 = b1 
a3 = a1 

d = n1 / m1
d1 = math.ceil(d)
d2 = d1 * b1

d3 = n2 * a1

while n3 >= m1:
    n3 = n3 - m1 
    sum1 = sum1 + b3
    
while n3 > 0:
    sum1 = sum1 + a3
    n3 = n3 - 1
    
    
print(min(d2,d3,sum1))


