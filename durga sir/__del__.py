import time
class Test:
    def __init__(self):
        print("Constuctor Execution")
    def __del__(self):
        print("Destructor Executions")

l=[Test(),Test(),Test()]
del l
time.sleep(5)
print("End Of Aplication")
