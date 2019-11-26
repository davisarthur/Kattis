# Davis Arthur
# 11-26-2019
# 2048

# omit zeros and cast each board entry to an integer
def omit(bd):
    newBoard = []
    for row in bd:
        newRow = []
        for num in row:
            if int(num) != 0:
                newRow.append(int(num))
        newBoard.append(newRow)
    return newBoard

# transpose the board
def transpose(bd):
    newBoard = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            newBoard[i][j] = bd[j][i]
    return newBoard

# reverse rows
def reverse(bd):
    newBoard = []
    for row in bd:
        newRow = []
        i = 3
        while i > -1:
            newRow.append(row[i])
            i = i - 1
        newBoard.append(newRow)
    return newBoard

# swipe left
def left(bd):
    bd = omit(bd)
    newBoard = []
    for row in bd:
        newRow = []
        i = 0
        while i < len(row):
            if i < len(row) - 1 and row[i] == row[i + 1]:
                newRow.append(row[i] + row[i + 1])
                i = i + 2
            else:
                newRow.append(row[i])
                i = i + 1
        while len(newRow) < 4:
            newRow.append(0)
        newBoard.append(newRow)
    return(newBoard)

# swipe right
def right(bd):
    bd = reverse(bd)
    bd = left(bd)
    return reverse(bd)

# swipe up
def up(bd):
    bd = transpose(bd)
    bd = left(bd)
    return transpose(bd)

# swipe down
def down(bd):
    bd = transpose(bd)
    bd = right(bd)
    return transpose(bd)

# read in board
line1 = str(input()).split()
line2 = str(input()).split()
line3 = str(input()).split()
line4 = str(input()).split()
board = [line1, line2, line3, line4]

# recoginize control
control = int(input())
if control == 0:
    board = left(board)
elif control == 1:
    board = up(board)
elif control == 2:
    board = right(board)
elif control == 3:
    board = down(board)

# print board
for row in board:
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
