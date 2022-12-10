from random import *

#m=int(input("lenght of otp"))
n=int(input("Enter How Much OTP"))


for i in range(n):
    for j in range(2):
        x=randint(0,9)
        ch=chr(randint(65,90))
        print(str(x)+ch,end="")
        
    print("\n")

