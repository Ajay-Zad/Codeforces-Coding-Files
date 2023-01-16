Y = int(input())
while Y!=0:
    Y = Y - 1
    x = int(input())
    a,b,c = input().split()
    t = [0,0,0,0]
    t[1] = int(a)
    t[2] = int(b)
    t[3] = int(c)
    s=set()
    while x != 0:
        s.add(x)
        x = t[x]
    if len(s) == 3:
        print("YES")
    else:
        print("NO")
    
    