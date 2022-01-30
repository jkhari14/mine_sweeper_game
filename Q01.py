def print_status(width, height, status, neighbor_mine):
    board = [["[   ]" for j in range(width+1)] for i in range(height+1)]
    board[0][0] = "     "
    for j in range(1, width+1):
        board[0][j] = f"{j-1}    "
    for i in range(1, height+1):
       board[i][0] = f"{i-1}  "

    for i in range(1, height+1):
        for j in range(1, width+1):
            if status[i-1][j-1] == 'Flagged':
                board[i][j] = "[ F ]"
            elif status[i-1][j-1] == 'Explored':
                board[i][j] = f"[ {neighbor_mine[i-1][j-1]} ]"
            else:
                board[i][j] = "[   ]"

    for i in range(height+1):
        print(''.join(board[i]))


    



    







# Testing cases.
#Do not remove "if __name__ == '__main__':". It is to makes sure the code is executed
#when you test this function but will not be executed when we use the function in other places
if __name__ == '__main__':
    print_status(2, 2, [['None', 'None'], ['None', 'None']], [[0, 0],[0, 0]])
#expected result:
#   0 1
#0 | | |
#1 | | |

    print_status(2, 2, [['Explored', 'Explored'], ['Explored', 'Explored']], [[1, 2],[3, 4]])
#expected result:
#   0 1
#0 |1|2|
#1 |3|4|

    print_status(3, 3, [['Explored', 'Flagged', 'None'], ['None', 'Explored', 'Flagged'], ['None', 'None', 'None']], [[1, 2, 4],[2, 1, 1],[0, 0, 0]])
#expected result:
#   0 1 2
#0 |1|F| |
#1 | |1|F|
#2 | | | |
    print_status(4, 3, [['Explored', 'Flagged', 'None', 'None'], ['None', 'Explored', 'Flagged', 'None'], ['None', 'None', 'None', 'Flagged']], [[1, 2, 4, 0],[2, 1, 1, 1],[0, 0, 0, 1]])
#expected result:
#   0 1 2 3
#0 |1|F| | |
#1 | |1|F| |
#2 | | | |F|
