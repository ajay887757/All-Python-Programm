from abc import *
class loan(ABC):
    def getloanIntrest(self):
        pass
class Homeloan(loan):
    def getloanIntrest(self):
        return 8
class vihicleloan(loan):
    def getloanIntrest(self):
        return 12
class personalloan(loan):
    def getloanIntrest(self):
        return 22

h=Homeloan()
print(h.getloanIntrest())

v=vihicleloan()
print(v.getloanIntrest())

p=personalloan()
print(p.getloanIntrest())

    
    
        
