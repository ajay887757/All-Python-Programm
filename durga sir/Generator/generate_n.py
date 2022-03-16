from re import I


def generator(n):
    
    i=1
    while i<=n:
        yield i
        i=i+1

g=generator(10)
import time
for i in g:
    print(i)
    time.sleep(1)