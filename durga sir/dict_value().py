d={100:'A',200:'B',300:'C',400:'D'}
value=input("Enter Value")
available=False
for k,v in d.items():
    if v==value:
        print("The corresponding key",k)
        available=True
if available==False:
    print("the Value is not avialable in this dictonary {}".format(value))
    
