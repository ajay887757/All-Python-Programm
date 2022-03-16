x=input("Enter Any String")
m=input("Enter Substring you want to find:")
f=x.find(m)
c=x.count(m)
for i in x:
    if f==-1:
        continue
    print("Substrinhg ={} find at index={}".format(m,f))
    f=x.find(m,f+1,len(x))
print("Total Number of Substring {} is= {}".format(m,c))
        
    
