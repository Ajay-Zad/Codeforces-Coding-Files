import math
t = int(input())
i = 0 
while i < t:
    i += 1
    n1,m1 = input().split()
    n = int(n1)
    m = int(m1)
    o = (n*m) / 2
    print(math.ceil(o))