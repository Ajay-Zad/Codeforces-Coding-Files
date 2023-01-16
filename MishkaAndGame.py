n = int(input())
i = 0
a = 0
b = 0
while i < n:
    m1,c1 = input().split()
    m = int(m1)
    c = int(c1)
    if m > c:
        a+=1
    elif c > m :
        b+=1
    else:
        pass
    i+=1
        
if a > b:
    print("Mishka")
elif b > a:
    print("Chris")
else:
    print("Friendship is magic!^^")
        