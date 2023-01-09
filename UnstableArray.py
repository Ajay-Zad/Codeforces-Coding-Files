t = int(input())
i = 0 
while i < t :
    n1,m1 = input().split()
    n = int(n1)
    m = int(m1)
    r = min(2,n-1) * m
    print(r)
    i += 1