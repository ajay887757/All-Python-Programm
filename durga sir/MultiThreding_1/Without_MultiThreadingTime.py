import time 


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
double(numbers)
square(numbers)
endtime=time.time()

print("The Total Time Taken : ",endtime-begintime)