s = input()
a = []
s1 = ''
for i in s:
    if i == '+':
        s = s.replace('+','')
        
for i in s:
    a.append(i)

a.sort()

for i in a:
    s1 = s1 + i+"+"
    
print(s1[:(len(s1)-1)])