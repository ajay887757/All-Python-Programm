x=input("Enter Any String")
for i in x:
    if i>=chr(65) and i<=chr(90):
        f=x.find(i)
        print(f)
