n = int(input())
l = []
l1 = []
x = [int(x) for x in input().split()]
l.append(x)
y = [int(y) for y in input().split()]
l1.append(y)
l3 = []
l4 = []
x1 = 0
for i in l:
    for j in i:
        x1+=1
        if x1== 1:
            continue
        l3.append(j)

y1 = 0        
for i in l1:
    for j in i:
        y1+=1
        if y1 == 1:
            continue
        l4.append(j)
        

l5 = []
l5.append(l3)
l5.append(l4)
l6 = []
for i in l5:
    for j in i:
        l6.append(j)
 
l6.sort()
s = set(l6)

l8 = []
for i in range(0,n):
    j+=1
    l8.append(j)
    
s1 = set(l8)

if len(s1) == len(s):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")