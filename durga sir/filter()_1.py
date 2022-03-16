l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1=list(filter(lambda x:x%2==0,l))
print("Even List Is:-",l1)

l2=list(filter(lambda x:x%2!=0,l))
print("odd List Is:-",l2)
