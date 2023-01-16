s = "writeInTheEditor"
sum1 = ""
l = []
for i in s:
    if i.islower():
        sum1 = sum1 + i
    else:
        l.append(sum1)
        sum1 = ""
        sum1 = sum1 + i

l.append(sum1)
l1 = []       
cnt = 0
for i in range(0,len(l)):
    if cnt == 0:
        l[i] = l[i].upper()
        cnt = cnt + 1
    else:
        s1 = l[i]
        s2 = s1[:1]
        s3 = s1[1:len(s1)]
        s4 = s2.lower()
        l[i] = s4+s3.upper()
    
for i in l:
    print(i)
    
            
            
        