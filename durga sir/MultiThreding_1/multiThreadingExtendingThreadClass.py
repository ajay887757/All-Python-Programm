from threading import *

class MyThread(Thread):
    def run (self):
        for i in range(10):
            print("child Thrread \n")


obj=MyThread()
obj.start()
for i in range(10):
    print("Main Thred \n")
