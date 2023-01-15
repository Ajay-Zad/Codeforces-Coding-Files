for _ in range(int(input())):
    n = int(input())
    s = input()
    sum1 = ""
    for i in s:
        if i == 'U':
            sum1 = sum1 + 'D'
        elif i == 'D':
            sum1 = sum1 + 'U'
        else:
            sum1 = sum1 + i
    print(sum1)
        