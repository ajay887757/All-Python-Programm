class Parent:
    def property(self):
        print("Land+Gold+Cash")
    def merry(self):
        print("Arunima")

class Child(Parent):
    def merry(self):
        super().merry()
        print("Pratibha")

c=Child()
c.merry()