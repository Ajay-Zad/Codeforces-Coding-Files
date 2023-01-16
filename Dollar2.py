n = int(input("enter the value for n :"))
n1,n2,n3,n4,n5,r1,r2,r3,r4 = 0,0,0,0,0,0,0,0,0
if n >= 100:
    n1 = n // 100
    r1 = n % 100
    if r1 == 0:
        print(n1)
        
if r1 >= 20:
    n2 = r1 // 20
    r2 = r1 % 20
    if r2 == 0:
        print(n1+n2)
        
if r2 >= 10:
    n3 = r2 // 10
    r3 = r2 % 10
    if r3 == 0:
        print(n1+n2+n3)
        
if r3 >= 5:
    n4 = r3 // 5
    r4 = r3 % 5
    if r4 == 0:
        print(n1+n2+n3+n4)
        
if r4 >= 1:
    n5 = r4 // 1
    print(n1+n2+n3+n4+n5)