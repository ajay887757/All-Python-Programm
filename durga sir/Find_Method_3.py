x='abcdefghijklmnopqrstuvwxyz'
y='zyxwvutsrqponmlkjihgfedcba'
n=input("Enter String")
for i in n:
    f=x.find(i)
    #print(f,end="")
    u=y[f]
    print(u,end="")
    
