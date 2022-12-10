l=['Katrinakaif','rakul','Kareenakapoor','Shradhakapoor','Alia','Sonam']
l1=list(filter(lambda x:x[0]=='K',l))
print(l1)

l2=list(filter(lambda x:len(x)%2==0,l))
print(l2)
