from threading import *

class A(Thread):
    def run(self):
        for i in range(10):
            print("Chlid Thred",i)
            print("Current Thread of Class A:",current_thread().getName())

a=A()
a.start()

print("Out Side of Class Current Thread",current_thread().getName())
