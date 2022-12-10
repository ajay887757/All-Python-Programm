x=input("Enetr String:")
y=input("Enter SubString")
try:
    i=x.index(y)
    while True:
        print(i)
        try:
            i=x.index(y,i+len(y),len(x))
        except ValueError:
            print("Total Number of{}".format(x.count(y)))
            break

except ValueError:
    print(" SunString Not Found")
