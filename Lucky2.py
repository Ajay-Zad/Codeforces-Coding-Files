import math
n1 = int(input())
n = ''
a = 0
n = str(n1)
l1 = list(n)
for i in l1:
    if i == '7' or i == '4':
        a+=1
    
if a == 7 or a == 4:
    print("YES")
else:
    print("NO")
