n = int(input())
a2 = 0
l1 = []
for i in range(0,n):
    a,b = input().split()
    a1 = int(a)
    b1 = int(b)
    c1 = abs(a1 - b1)
    d1 = (c1+8)//10
    l1.append(d1)
    
for i in l1:
    print(i)
    
            
        
        