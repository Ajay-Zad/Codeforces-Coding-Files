t = int(input())
while t != 0:
    t = t - 1
    n = int(input())
    s = input()
    se = set(s)
    cnt = 0
    l =[]
    for i in se:
        cnt = 0
        for j in range(0,len(s)):
            if i == s[j]:
                cnt = cnt+1
        l.append(cnt)

    l1 = []
    cnt = 1
    for i in l:
        if i >= 1:
            cnt = cnt * i + 1
        l1.append(cnt)
        cnt = 1
    print(sum(l1))
        

    
        
        