n = int(input())
l1 = []
l2 = []
for i in range(0,n):
    h,g = input().split()
    h1 = int(h)
    g1 = int(g)
    l1.append(h1)
    l2.append(g1)
a = 0    
for i in range(0,n):
    for j in range(0,n):
        if i!=j and l1[i] == l2[j]:
            a+=1

print(a)
            
    