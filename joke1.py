from collections import *
import sys
n,m = input().split()
n = int(n)
m = int(m)
aaa = [int(aaa) for aaa in input().split()]
bbb = [int(bbb) for bbb in input().split()]
a = Counter(aaa)
b = Counter(bbb)
aa = sum(aaa)
bb = sum(bbb)
cnt = 0
for k,v in a.items():
    if aa == bb:
        if v>1:
            print("Ambiguity")
            sys.exit()
if aa == bb:
    print("Possible")
    for i in aaa:
        print(i,"",end="")
else:
    print("Impossible")