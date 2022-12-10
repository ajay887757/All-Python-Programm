n=12

# if x<=1:
#     print("Not Prime")

# else:
#     isprime=True
#     for i in range(2,x):
#         if x%i==0:
#             isprime=False
#     if isprime==True:
#         print("is prime",x)
#     else:
#         print("Not Prime",x)

# n=int(input("Enter Value"))
count=0
n1=2
while True:
    is_prime=True
    for i in range(2,n1):
        if n1%i==0:
            is_prime=False
            break
    if is_prime==True:
        print("😊",n1)
        count=count+1
    if count==n:
        break
    n1=n1+1