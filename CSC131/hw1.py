"""
Kyle Finter
finter179
1/28/16
Homework 1 - CSC 131
Program that uses 2D lists to verify whether or not a Sudoku solution is valid
"""

def checkLst(lst):
    """returns True if list (may represent row, column or a block) has the values 1 to 9"""
    #replace pass by the necessary code
    pass
        

def isValid(grid):
    """returns True if solution is valid and False otherwise"""
    digitList=[1,2,3,4,5,6,7,8,9]
    #verify that every row has the numbers from 1 to 9
    for row in grid:
        currentRow=[]
        for number in row:
            if number not in digitList:
                return False
            else:
                if number not in currentRow:
                    currentRow.append(number)
                else:
                    return False

    #verify that every column has the numbers from 1 to 9
    rowCounter=0
    #columnCounter=0
    for columnNumber in range(0,9):
        currentColumn=[]
        for row in grid:
            if row[columnNumber] not in digitList:
                return False
            else:
                if row[columnNumber] not in currentColumn:
                    currentColumn.append(grid[rowCounter][columnNumber])
                else:
                    print('false2')
                    return False
            rowCounter+=1
        columnNumber+=1
        rowCounter=0

    #verify that every 3-by-3 box has the numbers from 1 to 9
    #Boxes will be processed in a left to right, top to bottom order
    startRow = 0 #row coordinate of starting cell in a 3-by-3 box
    startColumn = 0 #column coordinate of starting cell in a 3-by-3 box
    for boxNumber in range(0, 9): 
        currentBox = []
        for row in range(startRow, startRow + 3):
            for column in range(startColumn, startColumn + 3):
                currentBox.append(grid[row][column])
        #display(currentBox)
        if checkLst(currentBox) == False:
            return False
        startColumn += 3 #time to move to the next box
        if startColumn == 9: #time to move to the next row of boxes
            startColumn = 0
            startRow += 3
            
    #if here, then solution must have passed all verification
    return True 


def main():
    file_names_list = ["sudoku1.txt", "sudoku2.txt", "sudoku3.txt", "sudoku1b.txt", "sudoku2b.txt", "sudoku3b.txt"]
    
    for file_name in file_names_list:
        grid = [] #to store solution read from file
        f = open(file_name)
        for line in f:
            line = line.split()
            line = list(map(int, line)) # convert strings to integres
            grid.append(line)

        if isValid(grid):
            print("valid solution")
        else:
            print("invalid solution")
        
main()
