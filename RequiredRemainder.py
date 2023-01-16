t = int(input())
while t > 0:
    x1, y1, n1 = input().split()
    x = int(x1)
    y = int(y1)
    n = int(n1)
    if n-n % x+y <= n :
        print(n-n % x+y)
    else:
        print(n-n % x-(x-y))
    t -= 1
    