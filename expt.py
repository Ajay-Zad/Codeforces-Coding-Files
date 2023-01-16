flag = 1
while flag == 1:
    print("MENU\n1)Arithmetic exception\n2)Assertion\n3)index exception\n5)File exception\n6) Raise Exception")
    ch = int(input("enter the choice :"))
    if ch == 1:
        a = int(input("enter the value for a :"))
        b = int(input("enter the value for b :"))
        try:
            c = a / b
            print(c)
            print("Success")
        except ArithmeticError as e:
            print(e)
    elif ch == 2:
        a = int(input("enter the value for a :"))
        b = int(input("enter the value for b :"))
        try:
            assert a == b,"number mismatch"
            print("Success")
        except AssertionError as e:
            print(e)
    elif ch == 3:
        l1 = [1,2,3,4,5]
        a = int(input("enter the index to get the value :"))
        try:
            print("the value at the given index is :",l1[a])
            print("success")
        except IndexError as e:
            print(e)
    elif ch == 4:
        a = input("enter the name of the file :")
        b = input("enter the mode of access of the file :")
        try:
            f = open(a,b)
            f.write("AJAY ZAD")
            print("Success")
        except IOError as e:
            print(e)
    elif ch == 5:
        def age(num):
            try:
                if num <= 18:
                    raise Exception
            except Exception:
                return "NOT Eligible"
            else:
                return "Eligible"
        n = int(input("enter the age :"))
        print(age(n))
    flag = int(input("enter 1 to continue and 0 to exit :"))
                