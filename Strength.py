import sys
s,n = input().split()
s1 = int(s)
n1 = int(n)
l = []
l1 = [] 
for i in range(0,n1):
    x,y = input().split()
    x1 = int(x)
    y1 = int(y)
    l.append(x1)
    l1.append(y1)

for i in range(len(l)-1):
    for j in range(len(l)-1):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
            l1[j],l1[j+1] = l1[j+1], l1[j]
            
for i in range(0,n1):
    if s1 > l[i]:
        s1 = s1 + l1[i]
    else:
        print("NO")
        sys.exit()
    
print("YES")
        

        