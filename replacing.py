for _ in range(int(input())):
    n, x = input().split()
    x = int(x)
    n = int(n)
    l = [int(l) for l in input().split()]
    if n == 1:
        if l[0] % 2 == 0:
            print("NO")
            continue
        else:
            print("YES")
            continue
    if n == 2 and x == 1:
        for i in l:
            if i % 2 != 0:
                print("YES")
                break
        else:
            print("NO")
    
    if n == x:
        if sum(l) % 2 == 0:
            print("NO")
            continue
        else:
            print("YES")
            continue
        
    if n >= 3:
        e = []
        o = []
        for i in l:
            if i % 2 == 0:
                e.append(i)
            else:
                o.append(i)
        if x % 2 == 0 and len(o) == len(l):
            print("NO")
            continue
        cnt = 0
        if len(o) >= x:
            print("YES")
        else:
            sum1 = 0
            if len(o) % 2 == 0:
                cnt = x - (len(o)-1)
                for i in range(0,len(o)-1):
                    sum1 = sum1 + o[i]
            else:
                cnt = x - len(o)
                sum1 = sum(o)
            for i in e:
                sum1 = sum1 + i
                cnt = cnt + 1
                if cnt == x:
                    break
                
            if sum1 % 2 == 0:
                print("NO")
            else:
                print("YES")
                
            
            
       
            
        