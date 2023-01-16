t = int(input())
while t != 0:
    t = t - 1
    n  = int(input())
    l=[]
    for i in range(1,n+1):
        l.append(2**i)
     
    l1=[]
    l2=[]
    cnt = 0
    for i in l:
        if cnt % 2 == 0:
            l1.append(i)
            cnt = cnt + 1
        else:
            l2.append(i)
            cnt = cnt + 1
    print(l1)
    print(l2)
    sum1 = abs(sum(l1) - sum(l2))
    print(sum1)
            
    
        