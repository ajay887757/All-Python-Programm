# n=int(input("Enter Value"))
# count=0
# n1=2
# while True:
#     is_prime=True
#     for i in range(2,n1):
#         if n1%i==0:
#             is_prime=False
#             break
#     if is_prime==True:
#         print(n1)
#         count=count+1
#     if count==n:
#         break
#     n1=n1+1

def n_primes(N):
    primes=[]
    checkthis=2
    while len(primes)<N:
        ptest=[checkthis for i in primes if checkthis%i==0]
        primes+=[] if ptest else[checkthis]
        checkthis+=1
    return primes

l=n_primes(100)
print(l)
print(len(l))
