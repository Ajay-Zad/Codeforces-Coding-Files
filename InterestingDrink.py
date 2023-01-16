n = int(input())
x = [int(x) for x in input().split()]
q = int(input())
while q > 0:
    m = int(input())
    cnt=0
    for j in x:
        if m >= j:
            cnt+=1
    print(cnt)
    q-=1
    
            