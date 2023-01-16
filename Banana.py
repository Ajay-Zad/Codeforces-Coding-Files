k,n,w = input().split()
w1 = 0
for i in range(1,int(w)+1):
    w1 = w1 + i * int(k)

w2 = w1 - int(n)
if w2 > 0:
    print(w2)
else:
    print("0")

    
    