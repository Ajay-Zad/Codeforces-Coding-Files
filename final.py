t = int(input())
while t!=0:
    t = t - 1
    x = [int(x) for x in input().split()]
    s5 = max(x[0],x[1])
    s6 = max(x[2],x[3])
    
    s7 = min(s5,s6)
    cnt = 0
    for i in x:
        if i > s7:
            cnt = cnt + 1
    if cnt == 2:
        print("NO")
    else:
        print("YES")
    
    