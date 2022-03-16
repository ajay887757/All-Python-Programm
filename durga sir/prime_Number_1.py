n=int(input("Enter n Value"))
n1=2
c=0
while n1<=n:
    is_prime=True
    for i in range(2,n1//2+1):
        if n1%i==0:
            is_prime=False
            break
    if is_prime==True:
        print("Prime Number",n1)
        c=c+1
        print(c)
    n1=n1+1
    
