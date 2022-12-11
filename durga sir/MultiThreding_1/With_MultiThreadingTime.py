import time 
from threading import *

def double(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double: ",2*n)
def square(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square: ",n*n)

begintime=time.time()
numbers=[1,2,3,4,5,6,7]
t1=Thread(target=double,args=(numbers,))
t2=Thread(target=square,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime=time.time()

print("The Total Time Taken : ",endtime-begintime)