t = int(input())
i = 0
while i < t:
    n = int(input())
    x = [int(x) for x in input().split()]
    x.sort()
    result = x[n-1]-x[0]
    for a in range(0,n):
        for b in range(a+1,n):
            result = min(result,x[b]-x[a])
    print(result)
    i += 1
    