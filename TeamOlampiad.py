t = int(input())
x = [int(x) for x in input().split()]
a = 0 
b = 0 
c = 0
l = []
for i in range(0,len(x)):
    if x[i] == 1:
        l.append(i)
        a += 1
    elif x[i] == 2:
        b += 1
        l.append(i)
    else:
        c += 1
        l.append(i)
    
d = min(a,b,c)
print(d)

        
        
        
        