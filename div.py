t = int(input())
while t!=0:
    t = t - 1
    n1,x1 = input().split()
    y = [int(y) for y in input().split()]
    y.sort()
    a = len(y) // 2
    p = []
    p = y[:a]
    q = []
    q = y[a:]
    cnt = 0
    for i,j in zip(p,q):
        c = i - j
        if abs(c) >= int(x1):
            cnt = cnt + 1
            pass
        else:
            print("NO")
            continue
    if cnt == len(p):
        print("YES")
    