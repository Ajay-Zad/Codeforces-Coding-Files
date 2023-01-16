t = int(input())
l=[]
while t!=0:
    n = input()
    l.append(n)
    t = t - 1
    
s = set(l)
l1 =[]
for i in s:
    l1.append(l.count(i))
    
a = max(l1)
for i in s:
    if l.count(i) == a:
        print(i)
        break
        