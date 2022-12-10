m=int(input("Enter No Of row"))
n=int(input("Enter No Of col"))
a=[]
for i in range(m):
    b=[]
    for j in range(n):
        j=input("Enter Element in pocket ["+str(i)+"]["+str(j)+"]")
        b.append(j)
    a.append(b)
print("Matrix is ......")
print(a)   #[['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['M', 'N', 'O', 'P']]

for i in range(m):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
row=0
col=0
while row<m and col<n:
    for i in range(col,n):
        print(a[row][i],end=" ")
    row=row+1

    for i in range(row,m):
        print(a[i][n-1],end=" ")
       #print("HEllo")                                  #A B C D
                                                        #E F G H
                                                        #I J K L
                                                        #M N O P
    n=n-1
    if row<m:
        for i in range(n-1,(col-1),-1):
            print(a[m-1][i],end= " ")
        m=m-1
    if col<n:
        for i in range(m-1,row-1,-1):
            print(a[i][col],end=' ')
        col=col+1


# names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
# names2 = names1
# names3 = names1[:]

# names2[0] = 'Alice'
# names3[1] = 'Bob'

# sum = 0
# for ls in (names1, names2, names3):
#     if ls[0] == 'Alice':
#         sum += 1
#         print(sum)
#     if ls[1] == 'Bob':
#         sum += 10

# print (sum)