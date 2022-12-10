x=153
s=0
temp=x
while temp>0:
    tt=temp %10
    s=s+tt**3
    temp=temp//10

if s==x:
    print("Arm Strong")
else:
    print("Not armstrong")
