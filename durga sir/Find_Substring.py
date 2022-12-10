x=input("Enter String:")
y=input("Enter Substring")
i=x.find(y)
if i==-1:
    print("Not Found")
while i!=-1:
    print(i)
    i=x.find(y,i+len(y),len(x))

    
