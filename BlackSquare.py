b1,b2,b3,b4 = input().split()
a1 = int(b1)
a2 = int(b2)
a3 = int(b3)
a4 = int(b4)
x = input()
sum1 = 0
for i in range(0,len(x)):
    if x[i] == '1':
        sum1 = sum1 + a1
    elif x[i] == '2':
        sum1 = sum1 + a2
    elif x[i]== '3':
        sum1 = sum1 + a3
    else:
        sum1 = sum1 + a4
   
    
print(sum1)
    