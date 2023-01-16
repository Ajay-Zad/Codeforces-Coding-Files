import sys
n1,m1 = input().split()
n = int(n1)
m = int(m1)
for i in range(0,n):
    x = [x for x in input().split()]
    for j in x:
        if j == 'C' or j == 'M' or j == 'Y':
            print("#Color")
            sys.exit()
else:
    print("#Black&White")
    
    