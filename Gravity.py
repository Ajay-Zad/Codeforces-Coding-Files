n = int(input())
l = []
l2 = []
x = [int(x) for x in input().split()]
l.append(x)
for i in l:
    for j in i:
        l2.append(j)
        
l2.sort()
for i in l2:
    print(i,"",end='')
        