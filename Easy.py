n = int(input())
c = [int(x) for x in input().split()]
for i in c:
    if i == 0:
        pass
    else:
        print("HARD")
        break
else:
    print("EASY")