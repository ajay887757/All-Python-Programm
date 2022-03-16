x=input("Enter First Account Number :")
y=input("Enter Second Account Number :")

if x.isdigit():
    print("Is Digit Is Executed")
    if int(x)==int(y):
        print("Account Number is Matched")

        print(int(x))
    else:
        print("Account Is Not Matched")
else:
    print("String Is Eecuted")

    if x==y:
        print("IFSC code matched is Matched")

        print(x)
    else:
        print("IFSC code Not matched Matched")



