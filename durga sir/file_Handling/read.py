f=open("abc1.txt","r")

# data=f.read()

# data=f.read(3)
# data=f.readline()
# print(data)
data=f.readlines()

for i in data:
    print(i,end="")

f.close()


