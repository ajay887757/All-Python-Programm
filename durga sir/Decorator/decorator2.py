def deco(func):
    def inner(a,b):
        if b==0:
            print("Hello Stupid Please provide Correct Input")
            # return("Hello Stupid Please provide Correct Input")
        else:
            func(a,b)
            
    return inner
@deco
def division(a,b):
    print(a/b)
division(10,0)
# print(division(10,0))

# dec_for=deco(division)
# dec_for(10,0)