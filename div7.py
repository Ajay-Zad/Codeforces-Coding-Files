for _ in range(int(input())):
    n = int(input())
    if n % 7 == 0:
        print(n)
    else:
        if n <= 9:
            print("7")
            continue
        n2 = n // 10
        for i in range(n2*10,(n2*10)+10):
            if i % 7 == 0:
                print(i)
                break
                