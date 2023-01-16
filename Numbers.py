n = int(input())
x = [int(x) for x in input().split()]
h = x[0]
l = x[0]
a = 0 
for i in range(0,n):
    if x[i] > h:
        h = x[i]
        a+=1
        
    if x[i] < l:
        l = x[i]
        a+=1
        
print(a)
    