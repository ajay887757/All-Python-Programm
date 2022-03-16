def fibonacci(n):
    a,b=0,1
    count=1
    while True:
        if count<=n:
            yield a
            a,b=b,a+b
            # a=b
            # b=a+b
            count+=1
        else:
            break

        
g=fibonacci(10)
for i in g:
    print(i)