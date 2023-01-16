def aa(a):
    while a <= len(x)-1:
        x[a] = x[a] + 1
        a = a + 2
    cnt,cnt1 = 0,0
    for i in x:
        if i % 2 == 0:
            cnt = cnt + 1
        else:
            cnt1 = cnt1 + 1
    return cnt,cnt1
    
t = int(input())
while t != 0:
    t = t - 1
    n = int(input())
    x = [int(x) for x in input().split()]
    a = 0
    cnt,cnt1 = aa(a)
    if cnt == len(x) or cnt1 == len(x):
        print("YES")
        continue
    a = 1
    cnt,cnt1 = aa(a)
    if cnt == len(x) or cnt1 == len(x):
        print("YES")
    else:
        print("NO")
    
    
    
        
        
        
        
        
    