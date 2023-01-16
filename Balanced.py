t = int(input())
l1 = []
for i in range(0,t):
    n = int(input())
    l1.clear()
    if n % 4 == 0:
        for j in range(1,n+1):
            if j % 2 == 0:
                l1.append(j)

        for j in range(1,n+1):
            if j % 2 == 1:
                if j == n-1:
                    j1 = j + int(n/2)
                    l1.append(j1)
                else:
                    l1.append(j)
                 
        print("YES")
        for i in l1:
            print(i,end=" ")
    else:
        print("NO")
                
        
        
                
                
            