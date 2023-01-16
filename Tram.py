n = int(input())
l = []
l1 = []
x2 = 0
for i in range(0,n):
    x,y = input().split()
    l.append(x)
    l1.append(y)
 
x1 = 0 
for i in range(0,n):

    x1 = x1 + int(l1[i]) - (int(l[i]))
    if int(x1) > x2:
        x2 = int(x1)
 
print(x2)
    

    
    