t = int(input())
while t != 0:
    t = t - 1
    n,m,x = input().split()
    n = int(n)
    m = int(m)
    x = int(x)
    x = x - 1
    col = x//n
    row = x % n
    print(row*m+col+1)
                
    