t = int(input())
while t != 0 :
    t = t - 1
    x1,n1,m1 = input().split()
    x = int(x1)
    n = int(n1)
    m = int(m1)
    cnt=1
    if 10*m >= x:
        print("YES")
        continue
    else:
        for i in range(0,n):
            if x >= 0:
                x = (x//2) + 10
            else:
                cnt = 0
        
        if cnt != 0:
            for i in range(0,m):
                if x >= 0:
                    x = x - 10
                
        if x > 0:
            print("NO")
        else:
            print("YES")
                
           
                
                
                
