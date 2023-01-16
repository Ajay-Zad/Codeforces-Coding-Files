t = int(input())
while t != 0:
    t = t - 1
    a1,b1 = input().split()
    a = int(a1)
    b = int(b1)
    if a == 0:
        print("1")
    elif a == 0 and b == 0:
        print("1")
    else:
        sum1 = 0
        sum1 = a + (b*2)
        print(sum1+1)
    