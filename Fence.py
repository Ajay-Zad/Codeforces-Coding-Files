n,h = input().split()
a = 0
n1 = int(n)
h1 = int(h)
l = []
p = [int(x) for x in input().split()]
l.append(p)
    
for i in l:
    for j in i:
        if j > h1:
            a+=1
            
print(n1+a)