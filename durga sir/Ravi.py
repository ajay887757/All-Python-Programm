def updating_required_numbers(matrix):
    new_matrix =[]
    for row in matrix:
        print("Row",row)   #
        print("Row count",row.count(-1))  #
        if row.count(-1) == 1:
            sum_of_row = sum(row)
            print("Sum of row",sum_of_row)   #
            requried_number = 14 - sum_of_row
            print("requried_number",requried_number) #
            indexing_of_required_number = row.index(-1)
            print("Indexing",indexing_of_required_number)    #
            row[indexing_of_required_number] = requried_number

            print("row after",row)
        new_matrix.append(row)
    return new_matrix

def transpose_of_matrix(matrix):
    print("Matrix",matrix)  #
    transepose_matrix = []
    for i in range(len(matrix)):
        column=[]
        for j in range(len(matrix)):  #for j in range(3):
            print("j",j) 
            print("i",i)              
            column.append(matrix[j][i])
            print("column",column)
        transepose_matrix.append(column)
    return transepose_matrix
    
given_input = [[-1,1,-1],[3,-1,7],[4,-1,2]]
updated_matrix = updating_required_numbers(given_input)
print("updated_matrix",updated_matrix)
transepose_matrix = transpose_of_matrix(updated_matrix)
print("transepose_matrix",transepose_matrix)
updated_matrix = updating_required_numbers(transepose_matrix)
print("updated_matrix",updated_matrix)
reverted_matrix = transpose_of_matrix(updated_matrix)
print("reverted_matrix",reverted_matrix)

for i in reverted_matrix:
    print(i)