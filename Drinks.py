n = int(input())
x = [int(x) for x in input().split()]
l = []
l.append(x)
l1 = []
sum1 = 0
for i in l:
    for j in i:
        l1.append(j)
        

for i in l1:
    sum1 = sum1 + i
    
print(sum1/n)