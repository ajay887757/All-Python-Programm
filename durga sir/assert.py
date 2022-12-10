
# Assert is used for debuging


def squareit(x):
    
    return x**x
assert squareit(2)==4 ,"Squareit of 2 is 4"
assert squareit(3)==9,"Squareit of 3 is 9"
assert squareit(4)==16,"Squareit of 4 is 16"

print(squareit(2))  #4
print(squareit(3))  #27
print(squareit(4)) # 256

# desable assert

# py -O assert.py