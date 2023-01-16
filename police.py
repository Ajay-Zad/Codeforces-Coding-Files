n = int(input())
x = [int(x) for x in input().split()]
sum1 = 0
a = 0
for i in range(0,n):
    if x[i] > 0:
        sum1 = sum1 + x[i]
    else:
        if sum1 > 0:
            sum1 = sum1 - 1
        else:
            a = a + 1
            
print(a)