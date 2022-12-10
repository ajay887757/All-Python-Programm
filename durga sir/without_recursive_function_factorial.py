def factorial(n):
    result=1
    while n>=1:
        result=result*n
        n=n-1
    #print(result)
    return result
    
#factorial(10)
r=factorial(int(input("Enter Number")))
print("The Factorial of ",r)
