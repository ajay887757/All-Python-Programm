class Book:
    def __init__(self,pages):
        self.pages=pages
    
    def __add__(self,others):
        return Book(self.pages+others.pages)
    
    def __str__(self):
        return "The Total Numbers of pages :{}".format(self.pages)

    def __mul__(self,others):
        return Book(self.pages*others.pages)
    
b1=Book(100)
b2=Book(200)
b3=Book(500)
b4=Book(600)
print(b1+b2)
print(b1+b2+b3)
print(b1+b2+b3+b4)
print(b1*b2+b1+b3)
print(b1+b2*b3+b4)
