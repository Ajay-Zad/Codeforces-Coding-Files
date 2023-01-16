t = int(input())
while t != 0 :
    t = t - 1
    n = int(input())
    x = [int(x) for x in input().split()]
    if x.count(1) % 2 == 0 and x.count(2) == 0:
        print("YES")
        continue
    elif x.count(2) % 2 != 0 and x.count(1) == 0:
        print("NO")
        continue
    elif sum(x) % 2 == 0:
        print("YES")
    else:
        print("NO")