s=input("Enter Your Name:")
f=input("You want to find alphabet in your name:")
x=s.find(f)
if x==-1:
    print("This Latter Not present in your name",f)
else:
    print("Congraculation latter finded {} index={}".format(f,x))
