n = int(input())
l = []
k1 = 0 
k = 0 
for i in range(0,n):
    c = [int(x) for x in input().split()]
    l.append(c)
    
for i in l:
    for a in i:
        if a <= 0:
            k1 = k1 + a
        
for j in l:
    for b in j:
        if b >= 0:
            k = k + b
    
k2 = k + k1
if k2 == 0:
    print("YES")
else:
    print("NO")
    
       
        
   