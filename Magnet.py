n = int(input())
l=[]
l1=[]
a=0
for i in range(0,n):
    c = input().split()
    l.append(c)
    
for i in l:
    for j in i:
        l1.append(j)
        
for i in range(1,n):
    if l1[i] == l1[i-1]:
        pass
    else:
        a+=1
        
print(a+1)