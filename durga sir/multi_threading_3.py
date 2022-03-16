from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("Child Thread-1")

m=MyThread()
m.start()

for i in range(10):
            print("Main Thread-1")