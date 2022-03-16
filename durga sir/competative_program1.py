l1=[]
l=[]
s=0
for i in range(int(input("Enter No :"))):    #1
    y= input("Enter Elemrnt")   # 3011
    print("y=",y)
    for j in y:
        # print("j=",j)
        l.append(j)          
    if y[1]=="0":
        p=0
        s=s+(int(l[0]+l[1])**int(l[2]))*int(l[-1])
        print(s)
    
    else:
        s=s+(int(l[1]+l[2])**int(l[0]))*int(l[-1])
        print(s)

print(l)
    
print("sum :",s)











# l=[1,2,3,3,3,3,2,2,2212]
# l.pop(1:4)
# print(l)