class Outer:
    def __init__(self):
        print("Outer Class Created..")
    class Inner:
        def __init__(self):
            print("Inner Class Created...")

        def m1(self):
            print("Inner Class Method")

#o=Outer()
#o.Inner().m1()

Outer().Inner().m1()
