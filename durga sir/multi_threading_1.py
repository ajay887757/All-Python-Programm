from threading import *

def display():
    print("This Code Executed by Child Thread:",current_thread().getName())

def display1():
    print("This Code Executed by Child Thread:",current_thread().getName())

t=Thread(target=display)
t.start()
t=Thread(target=display1)
t.start()
print("This Code Executed by Manin Thread:",current_thread().getName())
