def factorial(n):
    print("Execution of factorial function",n)
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
        print("Returning factorial ({}) is :{}".format(n,result))
    return result
r=factorial(3)
print("The Factorial ",r)
