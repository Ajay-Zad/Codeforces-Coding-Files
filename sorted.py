l1 = [1,4,6,8,11,13,1]
l2 = [1,2,7,9,10,12]
l3 = l1+l2
for i in range(0,len(l3)):
    for j in range(i,len(l3)):
        if l3[i] > l3[j]:
            temp = l3[i]
            l3[i] = l3[j]
            l3[j] = temp
print(l3)
           