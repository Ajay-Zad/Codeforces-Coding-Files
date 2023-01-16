for _ in range(int(input())):
    cnt = 0
    n = input()
    if n == '10000':
        print("1")
        print(n)
        continue
    n1 = int(n)
    if n1 <= 10:
        print("1")
        print(n1)
        continue
    l = []
    l1 = 0
    if cnt == 0:
        if len(n) == 4:
            l.append(n[0]+"000")
            l1 = l1 + 1
            if n[1] == '0':
                pass
            else:
                l.append(n[1]+"00")
                l1 = l1 + 1
                
            if n[2] == '0':
                pass
            else:
                l.append(n[2]+"0")
                l1 = l1 + 1
                
            if n[3] == '0':
                pass
            else:
                l.append(n[3])
                l1 = l1 + 1
                
        elif len(n) == 3:
            l.append(n[0]+"00")
            l1 = l1 + 1
            if n[1] == '0':
                pass
            else:
                l.append(n[1]+"0")
                l1 = l1 + 1
            if n[2] == '0':
                pass
            else:
                l.append(n[2])
                l1 = l1 + 1
        elif len(n) == 2:
            l.append(n[0]+"0")
            l1 = l1 + 1
            if n[1] == '0':
                pass
            else:
                l.append(n[1])
                l1 = l1 + 1
        else:
            pass
    print(l1)
    for i in l:
        print(i,"",end="")
    print()
            
             
          
          
            
    
    