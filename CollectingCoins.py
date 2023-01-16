import sys
t = int(input())
i = 0 
while i < t:
    i += 1
    a1,b1,c1,n1 = input().split()
    a = int(a1)
    b = int(b1)
    c = int(c1)
    n = int(n1)
    x = max(a,b,c)
    x1 = x - a
    x2 = x - b
    x3 = x - c
    x4 = x1+x2+x3
    n2 = x4 - n
    if n2 % 3 == 0 and x4 <= n:
        print("YES")
    else:
        print("NO")