def dec(fun):
    def inner(name):
        if name=="Sunny":
            print("Hello Sunny your very important for us ")
            print("Very very good morning")
        else:
            fun(name)
    return inner
@dec
def wish(name):
    print("Hello ",name,"Good Morning")

wish("Durga")
wish("Sunny")