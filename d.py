for _ in range(int(input())):
    a,b,k = input().split()
    a = int(a)
    b = int(b)
    k = int(k)
    k1 = k // 2
    if k % 2 == 0:
        sum1 = (a*k1) - (b*k1)
    else:
        sum1 = (a*(k1+1)) - (b*k1)
    print(sum1)