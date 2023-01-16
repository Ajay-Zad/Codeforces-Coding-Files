n = int(input())
l = []
a = [int(x) for x in input().split()]
c = 0
c1 = 0
j = 1
for i in range(1,n):
    if a[i] >= a[i-1]:
        c+=1
        c1 = max(c1,c)
    else:
        c = 0
        
if c1 > 0 or j == 1:
    print(c1+1)
else:
    print(c1)
