s=input("Enter Any Charcter")
if s.isalnum():
    print("It is AlphaNumeric")
    if s.isalpha():
        print("It is Alphabet symbol")
        if s.islower():
            print("It is lower case")
        else:
            print("It is upper case")
    else:
        print("It is digit")
elif s.isspace():
    print("It Is Space Charcter")
else:
    print("It is non space special charcters")
