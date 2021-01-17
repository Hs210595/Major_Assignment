#Sudoku Game Checker
def checkcolumn(col,Entry):
    for i in range(0,9):
        #print(sudoku[i][col])
        if sudoku[i][col]==Entry:
            return False
    return True
            

def checkarrow(row,Entry):
    for i in range(0,9):
        
        #print(sudoku[row][i])
        if sudoku[row][i]==Entry:
            return False
    return True
def checkcube(c,Entry):
    if c==1:
        for i in range(0,3):
            for j in range(0,3):
                print(sudoku[i][j])
                if sudoku[i][j]==Entry:
                    return False
        return True

    if c==2:
        for i in range(0,3):
            for j in range(6,9):
                if sudoku[i][j]==Entry:
                    return False
        return True
    if c==3:
        for i in range(0,3):
            for j in range(3,6):
                if sudoku[i][j]==Entry:
                    return False
        return True
    if c==4:
        for i in range(3,6):
            for j in range(0,3):
                if sudoku[i][j]==Entry:
                    return False
        return True
    if c==5:
        for i in range(3,6):
            for j in range(3,6):
                if sudoku[i][j]==Entry:
                    return False
        return True
    if c==6:
        for i in range(3,6):
            for j in range(6,9):
                if sudoku[i][j]==Entry:
                    return False
        return True
    if c==7:
        for i in range(6,9):
            for j in range(0,3):
                if sudoku[i][j]==Entry:
                    return False
        return True
    if c==8:
        for i in range(6,9):
            for j in range(3,6):
                if sudoku[i][j]==Entry:
                    return False
        return True
    if c==9:
        for i in range(6,9):
            for j in range(6,9):
                if sudoku[i][j]==Entry:
                    return False
        return True

print("Instruction")
print("1.Arrow and column  number start from the zero")
print("2.You have to enter the entry where is zero")

sudoku =    [
        [4, 1, 8, 5, 3, 7, 6, 2, 0],
        [7, 6, 9, 8, 0, 1, 4, 3, 5],
        [2, 3, 0, 4, 6, 9, 7, 1, 8],
        [0, 8, 7, 1, 4, 2, 3, 9, 6],
        [9, 2, 3, 7, 8, 0, 1, 5, 4],
        [6, 4, 1, 9, 5, 4, 2, 0, 7],
        [8, 9, 6, 0, 1, 4, 5, 7, 3],
        [1, 5, 4, 3, 7, 8, 0, 6, 2],
        [3, 7, 0, 6, 9, 5, 8, 4, 1]
]
for i in range(9):
    print(sudoku[i])

print("Enter the position of the entry you want to check")
while(1):
    for i in range(9):
        print(sudoku[i])
    x=int(input("Enter the row  position: "))
    y=int(input("Enter the column  position: "))
    z=int(input("Enter the value of cube number: "))

    entry=int(input("Enter the Entry: "))
    Value=int(checkcolumn(y,entry))
    Value=Value+int(checkarrow(x,entry))
    Value=Value+int(checkcube(z,entry))
    #print(Value)
    if Value==3:
        print("Entry is correct")
        sudoku[x][y]=entry
    else:
        print("Wrong Entry")



    




