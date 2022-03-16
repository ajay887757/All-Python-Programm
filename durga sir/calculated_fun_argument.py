t=10
a=14

def m1(a,b,c,d):
    print(len(locals()))
    print(globals()["t"])
    print(globals().get("a"))
    global t
    t=555
    print(t)
    print(globals().get("a"))
    
    #print(a)
    #print(type(a))
    #print(len(a))

m1(3,7,89,"Ajay")

