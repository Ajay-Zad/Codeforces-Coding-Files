for _ in range(int(input())):
    l = []
    m = 0
    n = 0
    l = [input() for j in range(8)]
    for i in range(1,7):
        c1 = l[i-1].count('#')
        c2 = l[i].count('#')
        c3 = l[i+1].count('#')
        if c1 == 2 and c3 == 2 and c2 == 1:
            for k in range(0,8):
                if l[i][k] == '#':
                    m = i 
                    n = k + 1
                    break
    print(m,n)            
                