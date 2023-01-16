n , l = input().split()
x = [int(x) for x in input().split()]
x.sort()
dis = 0 
for i in range(1,len(x)):
    dis1 = x[i] - x[i-1]
    if dis1 > dis:
        dis = dis1
        
if x[0] == 0 and x[len(x)-1] == int(l):
    dis = dis / 2
    print(dis)
else:
    print(dis)
    
