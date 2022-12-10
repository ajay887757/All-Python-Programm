
print("Index of element Without using collection")
x=[1,23,455,6]
chr=int(input("Enter Find Index Element"))
count=0

for i in x:
    if i!=chr:
        count=count+1

    else:
        break
print(chr,"present at ",count)