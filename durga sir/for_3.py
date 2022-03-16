from random import randint

n=int(input("Enter number "))
i=int(input("Enter 1st range:"))
j=int(input("Enter 2nd  range:"))

for x in range(n):
    for y in range(n):
        print(randint(i,j),end= " ")
    print()
