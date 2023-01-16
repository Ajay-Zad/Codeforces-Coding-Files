n = int(input())
s = input()
l = list(s)
k = 0
j = 0 
for i in range(1,n):
    if(l[i] == l[i-1]):
        k = k + 1
print(k)