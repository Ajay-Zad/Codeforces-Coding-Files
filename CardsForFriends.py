import sys
t = int(input())
i = 0
x = 0
while i < t:
    i += 1
    w1,h1,n1 = input().split()
    w = int(w1)
    h = int(h1)
    n = int(n1)
    x = 1
    while w % 2 == 0:
        w = w / 2
        x = x * 2
    while h % 2 == 0:
        h = h / 2 
        x = x * 2
    if x >= n:
        print("YES")
    else:
        print("NO")
        
        
    
        
    