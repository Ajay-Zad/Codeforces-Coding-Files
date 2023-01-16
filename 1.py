for _ in range(int(input())):
    l = []
    n = int(input())
    for i in range(0,n):
        x,y = input().split()
        l.append(int(x))
        l.append(int(y))
    sum1 = 0
    for i in l:
        sum1 = sum1 + (abs(i) * 2)
    print(sum1)

    