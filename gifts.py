n  = int(input())
x = [int(x) for x in input().split()]
if n % 2 == 1:
    for i in x :
        print(i,"",end="")
elif n == 2:
    for i in x :
        print(i,"",end="")
else:
    x1 = x[len(x)//2:]
    x1 = x1 + x[:len(x)//2]
    for i in x1:
        print(i,"",end="")
        
    