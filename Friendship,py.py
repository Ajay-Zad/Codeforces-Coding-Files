n = int(input())
s = input()
l = list(s)
a = 0
b = 0
for i in l:
    if i == 'A':
        a += 1
    else:
        b += 1
        
if a == b:
    print("Friendship")
elif a > b:
    print("Anton")
else:
    print("Danik")