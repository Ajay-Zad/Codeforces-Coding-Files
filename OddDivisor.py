import sys
t = int(input())
i = 0
while i < t:
    i += 1
    n = int(input())
    if (n & (n - 1)) != 0:
        print("YES")
    else:
        print("NO")