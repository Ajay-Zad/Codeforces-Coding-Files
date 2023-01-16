import math
import sys
n , k = input().split()

if int(n) % 2 == 0:
    n2 = int(n)// 2
else:
    n2 = int(n)/2
    n2 = math.ceil(n2)
    
if n2 >= int(k):
    print((2*int(k))-1)
    
if n2 < int(k):
    if int(n) % 2 == 1:
        k2 = int(k) - int(n)//2
        print((2*k2)-2)
        sys.exit()
    k1 = int(k) - int(n)//2
    print(2*k1)