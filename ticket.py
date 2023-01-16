t = int(input())
while t != 0:
    x = input()
    s1 = (x[:3])
    s2 = (x[3:])
    sum1 = 0
    sum2 = 0
    for i,j in zip(s1,s2):
       sum1 = sum1 + int(i)
       sum2 = sum2 + int(j)
    if sum1 == sum2:
        print("YES")
    else:
        print("NO")
    t = t - 1
    