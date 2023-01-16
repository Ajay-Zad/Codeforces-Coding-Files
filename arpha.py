import bisect
input()
a=sorted(map(int,input().split()))
for i in range(int(input())):
    print(bisect.bisect(a,int(input())))