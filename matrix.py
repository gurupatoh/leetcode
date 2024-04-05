def  search_matrix(matrix,target):
    if not matrix and not matrix[0]:
        return None
    rows=len(matrix)
    cols=len(matrix[0])
    
    row=0
    col=cols-1

    while(row<rows and col>=0):
        if (matrix[row][col]==target):
            return row,col
        elif(matrix[row][col]<target):
            row+=1
        else:
            col-=1
    return None
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
target = 6

result = search_matrix(matrix, target)
if result:
    print(f"Target {target} found at {result}")
else:
    print(f"Target {target} not found.")
            
