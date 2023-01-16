n = input()
l = list(n)
l.sort()
k = 0
for i in range(1,int(len(n))):
    if l[i] == l[i-1]:
        k = k + 1

a = len(n)-k
if a % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
