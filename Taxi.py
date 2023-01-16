import math

n = int(input())
c = [int(x) for x in input().split()]
c4 = 0
c3 = 0
c2 = 0
c1 = 0 
#c.sort(reverse=True)
for i in c :
    if i == 4:
        c4 = c4+1
        continue
    if i == 3:
        c3 = c3+1
        continue
    if i == 2:
        c2 = c2+1
        continue
    if i == 1:
        c1 = c1+1
        
car = c4
c4 = 0

if c1 > 0:
    car = car + min(c3, c1)
    c3 = c3 - min(c3,c1)
    c1 = c1 - min(c3,c1)
else:
    car = car + c3
    c3 = 0

if c3 > 0:
    car = car + c3

if c2 % 2 == 0:
    car = car + c2/2
    c2 = 0
else:
    car = car + c2/2
    c2 = 1

if c2 > 0:
    if c1 > 2:
        car = car + 1
        c2 = 0
        c1 = c1 - 2

if c1 > 0:
    if c1%4==0:
        car = car + c1/4
    else:
        car = car + math.ceil(c1/4)

print (int(car))