n = int(input())
x = [int(x) for x in input().split()]
a = 0
b = 0
a1 = 0
b1 = 0
for i in range(0,n):
    if x[i] % 2 == 0:
        a+=1
        b = i
    if x[i] % 2 == 1:
        a1+=1
        b1 = i
        
if a > a1:
    print(b1+1)
else:
    print(b+1)
    
    
        
    
    