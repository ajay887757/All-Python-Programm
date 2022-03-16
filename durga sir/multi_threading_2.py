from threading import *

def display():
    for i in range(10):
        print('Child Thread {i}: {c}'. format(i=i,c=current_thread().getName()))

# Thread(target=display).start()
t=Thread(target=display)
t.start()

for i in range(10):
        print('Main Thread {i}: {c}'. format(i=i,c=current_thread().getName()))
# print('Main Thread :', current_thread().getName())
