import numpy as np
grid = [["5","3","","","7","","","",""],
        ["6","","","1","9","5","","",""],
        ["","9","8","","","","","6",""],
        ["8","","","","6","","","","3"],
        ["4","","","8","","3","","","1"],
        ["7","","","","2","","","","6"],
        ["","6","","","","","2","8",""],
        ["","","","4","1","9","","","5"],
        ["","","","","8","","","7","9"]]

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

grids = np.array(grid)
for i in range(len(grids)):
    for j in range(len(grids[i])):
        if grids[i][j]=='':
            grids[i][j]=0

def making_board(grids):
    print("-------Sudoku Board---------")
    print("","--"*(len(grids[0])))
    for i in range(len(grids)):
        print("|",end=" ")
        for j in range(len(grids[i])):
            if ((j+1)%3 ==0):
                print(grids[i][j],end="|")
            else:
                print (grids[i][j],end=" ")
        print()
        if (i+1)%3 ==0:
            print("","--"*(len(grids[i])))
        

def empty(grids):
    for i in range(len(grids)):
        for j in range(len(grids[i])):
            if grids[i][j]=='0' or grids[i][j]==0:
                #print((i,j),end="  ")
                return (i,j) 
    return None    

def valid(grids,num,pos):
    #for rows
    for i in range(len(grids[0])):
        if grids[pos[0]][i] == str(num) or grids[pos[0]][i] == num:
            return False
    #for columns
    for i in range(len(grids)):
        if grids[i][pos[1]] == str(num) or grids[i][pos[1]] == num:
            return False
    #for boxes
    x_box = pos[0]//3
    y_box= pos[1]//3
    for i in range(x_box*3,x_box*3+3):
        for j in range(y_box*3,y_box*3+3):
            if grids[i][j]==str(num) or grids[i][j]==num:
                return False
    return True
    
def solve(grids):
    find = empty(grids)
    if not find:
        return True
    else:
        row,col=find
    for i in range(1,10):
        if valid(grids,i,(row,col)):
            grids[row][col]= i

            if solve(grids):
                return True
            grids[row][col]= 0  
    return False

    
    
        
making_board(grids)
print("--------------------------------------------------------")
solve(grids)
#print(valid(grids,8,(0,2)))
making_board(grids)
print("--------------------------------------------------------")
making_board(board)
print("--------------------------------------------------------")
solve(board)
making_board(board)
print("--------------------------------------------------------")