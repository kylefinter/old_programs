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
    rows=3
    columns=4
    counter=1
    for x in range(0,rows):
        row=input('Enter a '+str(rows)+'-by-'+str(columns)+' matrix row for row '+str(counter-1)+': ')
        row=row.split()
        matrix.append(row)
        counter+=1
    print('')
    #matrix=[[2.5,3,4,1.5],[1.5,4,2,7.5],[3.5,1,1,2.5]]
    displayMatrix(matrix)
    print('')
    for x in range(0,rows):
        sumColumn(matrix,columns)
Main()
