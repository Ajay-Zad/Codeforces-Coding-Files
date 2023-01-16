''' Author - Ajay Zad
    date   - 07/03/2022 ''' 

num = int(input("Enter the number :"))
string = str(num)
length = len(string)                    #Converting from int data type to string date type
if string[0] == string[length-1]:       #Comparing for equality
    print("Both are same")
else:
    print("Both are not same")
