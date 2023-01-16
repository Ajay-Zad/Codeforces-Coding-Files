t = int(input())
while t != 0:
    t = t - 1
    n = int(input())
    x = [int(x) for x in input().split()]
    m = min(x)
    sum1 = 0
    for i in x:
        sum1 = sum1 + (i-m)
    print(sum1)