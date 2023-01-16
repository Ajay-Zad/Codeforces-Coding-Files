t = int(input())
while t != 0 :
    t = t - 1
    n = int(input())
    x = [int((x)) for x in input().split()]
    y = []
    for i in x:
        if i % 2 != 0:
            y.append(i)
    sum1 = sum(y)
    if sum1 % 2 != 0:
        print("YES")
    else:
        print("NO")
        