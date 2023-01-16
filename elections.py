def ele(best,o1,o2):
    return max(0,(max(o1,o2)+1)-best)
t = int(input())
i = 0 
while i < t :
    a1,b1,c1 = input().split()
    a = int(a1)
    b = int(b1)
    c = int(c1)
    
    print(ele(a,b,c),"",ele(b,a,c),"",ele(c,a,b))
    i = i + 1
    