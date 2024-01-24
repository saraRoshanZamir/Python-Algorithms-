grid =[
    [0,0,0,0,6,0,0,0,0],
    [0,0,3,9,0,1,0,4,0],
    [1,0,0,0,0,0,0,0,7],
    [0,0,0,0,8,0,0,5,0],
    [0,0,6,0,4,0,0,0,0],
    [3,0,0,5,0,6,2,0,0],
    [0,0,1,3,0,5,0,9,0],
    [0,0,0,8,0,0,0,0,0],
    [0,9,0,0,0,0,4,0,0],
    
]


def valid_row(grid,row,column,number):
    if number in grid[row]:
        return False
    for x in range(9):
        if grid[x][column]==number:
            return False
    
    corner_row = row - (row % 3)
    corner_column = column - (column % 3)
    
    for i in range (3):
        for j in range (3):
            if grid[corner_row+i][corner_column+j]==number:
                return False
    return True
            
             
def solving(grid,row,column):
    if column==9:
        if row == 8:
            return True
        else:
            row+=1
            column=0
            
    if grid[row][column]>0:
        return solving(grid,row,column+1)
    
    for number in range (1,10):
        if valid_row(grid,row,column,number):
            grid[row][column]=number

            if solving(grid,row,column+1):
                return True
        grid[row][column]=0
    return False
        
   
if solving (grid ,0,0):
    for i in range (9):
        for j in range (9):
            print (grid[i][j],end=" ")
        print ("\n")  
else: print ( "there is no solution")