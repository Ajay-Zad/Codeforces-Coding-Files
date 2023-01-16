t = int(input())
i = 0
while i < t:
    x = []
    n = int(input())
    x = [int(x) for x in input().split()]
    
    sum1 = sum(x)    
    if sum1 == len(x):
        print("0")
    elif sum1 > len(x):
        sum2 = sum1 - len(x)
        print(sum2)        
    else:
        print("1")
    i = i + 1
        
                
            
        
        