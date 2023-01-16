t = int(input())
for i in range(0,t):
    a,b = input().split()
    a1 = int(a)
    b1 = int(b)
    if a1 % b1 == 0:
        print("0")
    else:
        c = b1 - (a1%b1)
        print(c)