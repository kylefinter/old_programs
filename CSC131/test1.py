def sumColumn(matrix, columnIndex):
    result=0
    for row in matrix:
        result=result+float(row[columnIndex])
    print('Sum of elements for column',str(columnIndex),'is',str(result))
def displayMatrix(matrix):
    newMatrix=[]
    print('The Matrix is')
    for row in matrix:
        for index in range(len(row)):
            row[index]=str(float(row[index]))
        newMatrix.append(row)
    for row in newMatrix:
        print(row[0],row[1],row[2],row[3])

def Main():
    matrix=[]
    row0=input('Enter a 3-by-4 matrix row for row 0: ')
    row1=input('Enter a 3-by-4 matrix row for row 1: ')
    row2=input('Enter a 3-by-4 matrix row for row 2: ')
    row0=row0.split()
    row1=row1.split()
    row2=row2.split()
    matrix.append(row0)
    matrix.append(row1)
    matrix.append(row2)
    print('')
    #matrix=[[2.5,3,4,1.5],[1.5,4,2,7.5],[3.5,1,1,2.5]]
    displayMatrix(matrix)
    print('')
    sumColumn(matrix,0)
    sumColumn(matrix,1)
    sumColumn(matrix,2)
    sumColumn(matrix,3)
Main()
