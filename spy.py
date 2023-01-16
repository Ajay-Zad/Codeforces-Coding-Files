t = int(input())
i = 0 
while i < t:
    n = int(input())
    a = [int(a) for a in input().split()]
    j = 1 
    while j <= len(a):
        if a[j] == a[j-1]:
            j = j + 1
        else:
            break
    if j == 1 and a[j] == a[j+1]:
        print(j)
    else:
        print(j+1)
    i = i + 1
    
        
    
    