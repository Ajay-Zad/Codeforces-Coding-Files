t = int(input())
while t != 0 :
    t = t - 1
    n = int(input())
    if n <= 1399:
        print("Division 4")
    elif n <= 1599 and n >= 1400:
        print("Division 3")
    elif n <= 1899 and n >=1600:
        print("Division 2")
    elif 1900 <= n:
        print("Division 1")
    else:
        pass
        