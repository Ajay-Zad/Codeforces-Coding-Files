t = int(input())
l1 = []
for i in range(0,t):
    a = int(input())
    if a % 2 == 0:
        a = a // 2 
        a = a - 1
        l1.append(a)
    else:
        a = a // 2
        l1.append(a)
        
for i in l1:
    print(i)
    
        
    