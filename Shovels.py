import sys
k, r = input().split()
k1 = int(k)
r1 = int(r)

a = k1 - r1 
if a % 10 == 0:
    print("1")
    sys.exit()

i1 = 1
while ((k1 * i1) % 10) - r1 != 0 and ((k1 * i1) % 10) != 0 :
    i1+=1       

print(i1)