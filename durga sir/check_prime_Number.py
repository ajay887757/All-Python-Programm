n=int(input("Enter Any Number :"))
if n<=1:
    print("It is not prime Number")
else:
    is_prime=True
    for i in range(2,n//2+1):
        if n%i==0:
            is_prime=False
            break
    if is_prime==True:
        print("It is prime Number")
    else:
        print("It is not prime Number")

    
