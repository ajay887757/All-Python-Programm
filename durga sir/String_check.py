# n=int(input('enter any number:'))
# j=0
# for i in range(n):
#     s=input('enter any string:')
#     k=s.split()
#     while j < len(k):
        
#         if j%2==0:
#             print('1')
#         else:
#             print('0')
#         j+=1


x=input("Enter String")     # SAJAPA    #SA@&AS
x1=x[1]
# print(x1)
# print(x.isalnum())

c=x.count(x1)
# print(c)
l=[]
if x.isalnum():
    for j in range(1,len(x),2):
        if x[j]==x1:
            l.append(x[j])
        else:
            l.clear()
            break
    if len(l)==c:
        print(1) 
    else:
        print(0)
else:
    print(0)

        
