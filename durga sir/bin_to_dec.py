
class bin:
    @staticmethod
    def dec(x):
        j=-1
        p=0
        s=0
        for i in x:
            y=x[j]
            c=int(y)*(2**p)
            s=s+c
            j=j-1
            p=p+1
        return s
#print(s)


d=bin()
x=input("Enter Binary Number [0/1]")
r=d.dec(x)
print("Decimal of {} is {}".format(x,r))


