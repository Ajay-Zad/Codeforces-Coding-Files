n = int(input())
l = []
for i in range(0,n):
    x = int(input())
    for i in range(2,x+1):
        if x % i == 0:
            l.append(i)
            continue
            
for i in l:
    if i % 2 == 1:
        print("yes")
    else:
        print("no")
        
    