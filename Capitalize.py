s = input()
j = 0
for i in s:
    j = j + 1
    if(j==1):
        s = i.capitalize()
        continue
    s = s + i
    
print(s)
    

