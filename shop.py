def dd(a,b,c):
    sum1 = (a*2) + (b*2)
    sum2 = a + b + c
    if sum1 >= sum2:
        return sum2
    else:
        return sum1

d1,d2,d3 = input().split()
d1 = int(d1)
d2 = int(d2)
d3 = int(d3)
d4 = max(d1,d2,d3)
if d4 == d1 and d4 == d2 and d4 == d3:
    sum1 = d1 + d2 + d3
    print(sum1)
elif d4 == d3:
    sum1 = dd(d1,d2,d3)
    print(sum1)
elif d4 == d2:
    sum1 = dd(d1,d3,d2)
    print(sum1)
else:
   sum1 = dd(d2,d3,d1)
   print(sum1)
    
    
