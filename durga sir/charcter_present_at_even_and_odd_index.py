x=input("Enter Any String:")
for i in x:
    f=x.find(i)
    if f%2==0:
        y=x[f]
        print("Even index charcter is {} and it index={}".format(y,f))
    else:
        z=x[f]
        print("Odd index charcter is {} and it index={}".format(z,f))
        
