n , m = input().split()
l = []
x = [int(x) for x in input().split()]
l.append(x)
l1 = []
for i in l:
    for j in i:
        l1.append(j)
l1.sort()       
l2 = []
for i in range(0,int(n)):
    l2.append(l1[i])
    
l3 = []
l1.sort(reverse=True)
for i in range(0,int(n)):
    l3.append(l1[i])
    
a = l2[int(n)-1]
b = l2[0]
    
A = l3[int(n)-1]
B = l3[0]

c = a - b 
C = A - B
if c > C and c >= 0 and C >= 0:
    print(C)
else:
    print(c)