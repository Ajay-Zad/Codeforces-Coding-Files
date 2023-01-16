def gcd(m,n):
    if m == 0:
        return n
    elif n == 0:
        return m
    else:
        return gcd(n,m%n)

a1,b1,n1 = input().split()
a = int(a1)
b = int(b1)
n = int(n1)

cnt = 0
while n != 0:
    if cnt % 2 == 0:
        cnt = cnt + 1
        g = gcd(a,n)
        n = n - g
        if n <= 0:
            print("0")
            break
    else:
        cnt = cnt + 1
        g = gcd(b,n)
        n = n - g
        if n <= 0:
            print("1")
            break
        
        
        
        

























