t = int(input())
while t!=0: 
    t = t - 1
    a1,b1,c1,x1,y1 = input().split()
    a = int(a1)
    b = int(b1)
    c = int(c1)
    x = int(x1)
    y = int(y1)
    sum1 = max(0,x-a) + max(0,y-b)
    if sum1 <= c:
        print("YES")
    else:
        print("NO")