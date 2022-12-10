def cal(a,b):
    sum=a+b
    sub=a-b
    mult=a*b
    div=a/b
    return sum,sub,mult,div
t1=cal(20,10)
s,*l=cal(200,100)
t,u,v,w=cal(2000,1000)
print(t1)
print(type(t1))
print(s)
print(type(s))
print(l)
print(type(l))

print("the sum is ",t)
print("The sunstraction",u)
print("The product",v)
print("The div",w)


for i in t1:
    print(i)

    
