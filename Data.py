n = int(input("enter the value for n :"))
l=[]
for i in range(0,n):
    l.append(input())
    
for i in range(0,n):
    if l[i] in l:
        print("YES")
        