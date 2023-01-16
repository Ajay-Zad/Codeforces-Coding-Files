t = int(input())
while t!=0:
    a1,b1,c1,d1 = input().split()
    l = []
    l.append(a1)   
    l.append(b1)  
    l.append(c1)  
    l.append(d1)  
    cnt = 0
    for i in l:
        if int(a1) < int(i):
            cnt = cnt + 1
    print(cnt)
    t = t - 1
    