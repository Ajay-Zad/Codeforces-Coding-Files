n = int(input())
a1 = 0
b1 = 0 
c1 = 0 
for i in range(0,n):
    a,b,c = input().split()
    a1 = a1 + int(a)
    b1 = b1 + int(b)
    c1 = c1 + int(c)
    
if a1 == 0 and c1 == 0 and b1 == 0:
    print("YES")
else:
    print("NO")
    