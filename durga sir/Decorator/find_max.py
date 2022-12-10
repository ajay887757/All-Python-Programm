l=[123,2,3,3,3,4,4,55,5,543]
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# print(max)

# min=l[0]
# for i in l:
#     if min>i:
#         min=i
# print(min)

l1=[]
while l:
    min=l[0]
    for i in l:
        if i<min:
            min=i
    l1.append(min)
    l.remove(min)
print(l1)






    