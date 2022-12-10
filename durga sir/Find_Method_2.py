x='abcdefghijklmnopqrstuvwxyz'
y='zyxwvutsrqponmlkjihgfedcba'
n=input("Enter String")
for i in n:
    f=x.find(i)
    if f==-1:
        continue
    else:
        #print(f,end="")
        v=y[f]
        print(v,end="")

