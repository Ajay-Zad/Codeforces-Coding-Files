s = input()
k = 0 
k1 = 0
for i in s:
    if(i=='0'):
        k = k + 1
        if k >= 7 :
            break
    else:
        k = 0
        
for i in s:
    if(i=='1'):
        k1 = k1 + 1
        if k1 >= 7:
            break
    else:
        k1 = 0
        
if( k >= 7 ):
    print("YES")
elif k1 >= 7:
    print("YES")
else:
    print("NO")
     