def decor(func):
    def inner():
        print("Sadi hue")
    return inner

@decor
def bhaiya():
    print("Jan Gana Se aaya hu Bhaiya :")

bhaiya()