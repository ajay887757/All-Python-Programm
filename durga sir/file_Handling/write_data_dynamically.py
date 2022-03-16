fname=input("Enter File Name :")
f=open(fname,"w")
while True:
    data=input("Enter Sone Data :")
    f.write(data+"\n")
    option=input("Do you want some more data [yes/no]")
    if option.lower()=="no":
        print("Thankyou Your Data is written successfully ")
        break
    else:
        continue

f.close()
