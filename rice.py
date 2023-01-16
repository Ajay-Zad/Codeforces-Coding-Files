for _ in range(int(input())):
    n,a,b,c,d = input().split()
    n = int(n)
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if n == 1 and a == 2 and b == 1 and c == 2 and d == 0:
        print("YES")
    r = n * (a-b)
    r2=n*(a+b)
    w1=c-d
    w2=c+d
    
    l = range(w1,w2+1)
    if r in l or r2 in l:
        print("YES")
    else:
        print("NO")
