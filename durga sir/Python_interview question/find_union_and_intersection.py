arr1=[1,3,4,5,7]
arr2=[2,3,5,6]

#Find union 

# Union1=arr1+arr2
# print(Union1)
# l=[]
# for i in Union1:
#     if i not in l:
#         l.append(i)
# print("Final Union",sorted(l))   #[1, 2, 3, 4, 5, 6, 7]

# find intersection
intersection=[]
for i in arr1:
    if i in arr2:
        intersection.append(i)
print("intersection",intersection)