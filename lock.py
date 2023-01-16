string = "hiHello"
result = ""
for i in string:
    if i.isupper():
        print(result)
        result = ""
        result += i.lower()
    else:
        result += i.upper()
print(result)

    




