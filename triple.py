from collections import *
t = int(input())
for _ in range(t):
	input()
	a = Counter(input().split())
    print(a)
	for k, v in a.items():
		if v>=3:
			print(k)
			break
	else:
		print(-1)