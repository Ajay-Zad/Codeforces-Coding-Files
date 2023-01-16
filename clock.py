for _ in range(int(input())):
    x = [x for x in input().split()]
    l1 = x[0].split(':')
    l2 = int(x[1])
    x1 = []
    for i in l1:
        x1.append(int(i))
    h = x1[0]
    if h == 22:
        print("1")
        continue
    m = x1[1]
    c = l2 // 60
    c1 = l2 % 60
    cc = 1
    cnt = 0
    cnt11 = 0
    if m == h and c == 24:
        print("1")
        continue
    try:
        ccc = 24//c
    except:
        cnt11 = 1
        
    if cnt11 == 0:
        while cc <= ccc:
            h = h + c
            m = m + c1
            
            sum3 = str(h)
            sum4 = str(m)
            sum3 = sum3 + sum4
            sum4 = sum3[::-1]
            if sum3 == sum4:
                cnt = cnt + 1
            cc = cc + 1
            if h == 24:
                h = 0
            if m == 60:
                m = 0
    else:
        hh = 0
        while hh <= 23:
            m = m + c1
            if m >= 60:
                h = h + 1
                hh = hh + 1
                m = m - 60
                if h == 24:
                    h = 0
            sum3 = str(h)
            sum4 = str(m)
            if sum3 <= '9':
                sum3 = '0' + sum3
            if sum4 <= '9':
                sum4 = '0' + sum4
            if int(sum3) >= 10:
                sum3 = sum3[1:]
            if int(sum4) >= 10:
                sum4 = sum4[1:]
            sum5 = sum3 + sum4
            print("sum = ",sum5)
            sum6 = sum5[::-1]
            if sum6 == sum5:
                cnt = cnt + 1
                print("the match",sum5)
    
    print(cnt)
            
            
            
        
    
    
    