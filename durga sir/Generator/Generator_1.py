def generator():
    yield "A"
    yield "B"
    yield "C"


# print(generator()) <generator object generator at 0x000001C1E1BB5C10>

g=generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

