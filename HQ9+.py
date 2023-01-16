s = input()
l = list(s)

for i in l:
    if i == 'H' or i == 'Q' or i == '9':
        print("YES")
        break
    else:
       pass
else:
    print("NO")