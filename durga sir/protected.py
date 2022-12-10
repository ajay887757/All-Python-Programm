class Test:
    def __init__(self,inital_balance):
        self._balance=inital_balance  # protected variable

    def m1(self):
        print("initial Balance: ",self._balance)
    
class SubTest(Test):
    pass

t=SubTest(1000)
t.m1()
print(t._balance)
