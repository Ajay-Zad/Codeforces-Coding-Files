n = int(input())
l = []
l1 = []
sum1 = 0
sum2 = 0
a = 0
c = [int(x) for x in input().split()]
l.append(c)
for i in l:
    for j in i:
        l1.append(j)
        
l1.sort(reverse=True)
for i in l1:
    sum1 = sum1 + i
    
s = sum1 / 2

for i in l1:
    if sum2 <= s:
        sum2 = sum2 + i
        a += 1
    else:
        break
    
print(a)

        
        

