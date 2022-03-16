l=eval(input("Enter List :"))
x=int(input("Enter element you want to remove:"))
if x not in l:
    print(x,"Not Avialable in your list")
else:
    while True:
        if x in l:
            l.remove(x)
        else:
            break
    print("After Removing",l)
