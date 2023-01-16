t = int(input("Test numbers size : "))
i = 0
l = []
while i < t:
    n = int(input("input the size of n: "))
    for j in range(0,n):
        m = int(input())
        l.append(m)
        
    sum1 = sum(l)
    
    if sum1 == len(l):
        print("0")
    elif sum1 > len(l):
        sum2 = sum1 - len(l)
        print(sum2)        
    else:
        print("1")
    l.clear()
    i = i + 1
        
                
            
        
        