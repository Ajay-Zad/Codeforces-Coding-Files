n = [4,1,-2,6,7,-3,-5]
l = []
l1 = []
for i in n:
    if i < 0:
        l.append(i)
    else:
        l1.append(i)
l2 =[]
cnt = 0
if n[0] > 0:
    for i,j in zip(l1,l):
        l2.append(i)
        l2.append(j)
    if len(l1) > len(l):
        l2.append(l1[len(l1)-1])
else:
    for i,j in zip(l1,l):
        l2.append(j)
        l2.append(i)
    if len(l) > len(l1):
        l2.append(l[len(l)-1])
    
            
print(l2)
        
    
    