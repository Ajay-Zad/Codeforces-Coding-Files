import sys
n = int(input())
x = [int(x) for x in input().split()]
 
m = max(x)
m1 = min(x)
i = 0
a1 = 0
if x[0] == m and x[(len(x))-1] == m1:
    print("0")
    sys.exit()
    
if len(x) == 2:
    print("1")
    sys.exit()
    
while i <= len(x)-1:
    if x[i] == m:
        a1 = i
        break
    i+=1
    
l1 = []
for i in range(len(x)-1,0,-1):
    l1.append(x[i])

b1 = 0 
j = 0 
while j <= len(x)-1:
    if l1[j] == m1:
        b1 = i 
        break
    j+=1
    
c = a1 + (n-b1)-1
print(c-1)