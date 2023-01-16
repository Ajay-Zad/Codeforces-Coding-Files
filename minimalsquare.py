t = int(input())
while t > 0 :
    a1,b1 = input().split()
    a = int(a1)
    b = int(b1)
    side = min(max(a*2,b),max(a,b*2))
    print(side*side)
    t -= 1