t = int(input())
while t!=0:
    t = t - 1
    a1,b1,n1 = input().split()
    a = int(a1)
    b = int(b1)
    n = int(n1)
    cnt = 0
    while a <= n and b <= n :
        if a <= b:
            a = a + b
            cnt = cnt + 1
        else:
            b = b + a
            cnt = cnt + 1
    print(cnt)
    
            
    
