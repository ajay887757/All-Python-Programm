from threading import *


def display2():
    print("Display_1 method")
    print("Current Thread Of display_1 Name :",current_thread().getName())
def display1():
    print("Display_2 method")
    for i in range(10):
        print("Current Thread Of display_2 Name :",current_thread().getName())

t1=Thread(target=display1)
t2=Thread(target=display2)
t1.start()
t2.start()

print("Current Thread Name :",current_thread().getName())