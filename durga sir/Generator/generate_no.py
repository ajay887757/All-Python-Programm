def generator(n):
    while n>=1:
        yield n
        n=n-1
g=generator(10)

for i in g:
    print(i)