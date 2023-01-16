import sys
n = int(input())
cnt = 0
l = []
if n == 3:
    print('1')
    print('3')
    sys.exit()
    
if n % 2 == 0:
    while n > 0:
        cnt+=1
        n = n - 2
        l.append('2')
    print(cnt)
    for j in l:
        print(j,end=' ')
else:
    while n > 0:
        cnt+=1
        n = n - 2
        l.append('2')
        if n == 3:
            n = n - 3
            cnt+=1
            l.append('3')
            break
    print(cnt)
    for j in l:
        print(j,end=' ')
           
        
    
       
        