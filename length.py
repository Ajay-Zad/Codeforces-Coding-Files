m1 ,s1 = input().split()
m = int(m1)
s = int(s1)
sum1 = s 
for i in range(0,m):
    for d in range(0,10):
        if((i > 0 or d > 0 or (m == 1 and d == 0)))