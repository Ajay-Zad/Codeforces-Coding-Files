t = int(input())
while 0 < t:
    n = int(input())
    i = 1
    j = 1
    while j == 1:
        if i % 3 == 0 or i % 10 == 3:
            i = i + 1
        else:
            n = n - 1
            if n == 0:
                print(i)
                break
            i = i + 1
        
    t = t - 1
        
            
            
        
            