def print_mine(width, height,mines):
    board = [["[   ]" for j in range(width+1)] for i in range(height+1)]
    board[0][0] = "     "
    for j in range(1, width+1):
        board[0][j] = f"{j-1}    "
    for i in range(1, height+1):
       board[i][0] = f"{i-1}  "

    for i in range(1, height+1):
        for j in range(1, width+1):
            if mines[i-1][j-1] == 1:
                board[i][j] = "[ * ]"
            else:
                board[i][j] = "[   ]"

    for i in range(height+1):
        print(''.join(board[i]))







#Testing cases.

if __name__ == '__main__':
    print_mine(2, 2,[[False, False],[False, False]])
#   0 1
#0 | | |
#1 | | |
    print_mine(2, 2, [[True, True],[True, True]])
#   0 1
#0 |*|*|
#1 |*|*|
    print_mine(3, 3, [[True, True, False],[False, True, False],[True, False, False]])
#   0 1 2
#0 |*|*| |
#1 | |*| |
#2 |*| | |
    print_mine(4, 3, [[True, True, False, False],[False, True, False, False],[True, False, False, True]])
#   0 1 2 3
#0 |*|*| | |
#1 | |*| | |
#2 |*| | |*|

