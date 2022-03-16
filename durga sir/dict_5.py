d=eval(input("Enter Dict"))
key=int(input("Enter key tou want to find"))
if key in d:
    print("The {} occurs {} the value".format(key,d[key]))
else:
    print("key is not available")

