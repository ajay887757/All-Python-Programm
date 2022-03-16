from random import choice

import time
name=["Sunny","Bunny","Ajay","Deepak"]
subject=["DBMS","Java","python","C"]

def student(n):
    l=[]
    for i in range(n):
        d={"id":i,"Name":choice(name),"Subject":choice(subject)}
        l.append(d)

    return l

t1=time.time()
x=student(100000)
f=open("Generator/abc.txt","w")
for i in x:
    f.write(str(i)+"\n")
print("Data Print Succesfully")

t2=time.time()

print("time taken in sec",t2-t1)



def Student_Generator(n):
    for i in range(n):
        d={"id":i,"Name":choice(name),"Subject":choice(subject)}
        yield d

t1=time.time()
g=Student_Generator(100000)
t2=time.time()

print("time taken in sec",t2-t1)


for i in g:
    # print(i)
    pass

t3=time.time()

print("time taken after Loop in sec",t3-t1)





    

