def uncover(statusMatrix, mineMatrix, neighborMatrix, i, j, height, width):
    if (i < 0 or i >= height or j < 0 or j >= width):
        return
    elif(mineMatrix[i][j] == True):
        return
    elif(neighborMatrix[i][j] == 0 and statusMatrix[i][j] != 'Explored'):
        statusMatrix[i][j] = 'Explored'
        direction = [0,1, 0,-1, 1,0, -1,0, 1,1, -1,-1, -1,1, 1,-1]
        for k in range(-1,14,2):
            uncover(statusMatrix, mineMatrix, neighborMatrix, i+direction[k+1], j+direction[k+2], height, width)
    elif statusMatrix[i][j] != 'Explored':
        statusMatrix[i][j] = 'Explored'
    else:
        return

def explore_board(i, j, status, mines, neighbor_mine, width, height):
    if (i < 0 or i >= height or j < 0 or j >= width):
        return False
    if status[i][j] == 'Flagged':
        return False
    if mines[i][j] == True:
        return True
    if status[i][j] == 'None' or status[i][j] == 'Explored':
        uncover(status, mines, neighbor_mine, i, j, height, width)
    return mines[i][j] == True 




#Testing cases.
if __name__ == '__main__': 
    status = [['None', 'None', 'None'],['None', 'None', 'None'],['None', 'None', 'Flagged']]
    #   0 1 2
    #0 | | | |
    #1 | | | |
    #2 | | |F|

    mines = [[True, True, False],[False, False, False],[False, False, True]]
    #   0 1 2
    #0 |*|*| |
    #1 | | | |
    #2 | | |*|

    neighbor_mine = [[1,1,1], [2,2,2], [0,1,0]]
    #   0 1 2
    #0 |1|1|1|
    #1 |2|2|2|
    #2 |0|1|0|

    hit = explore_board(1, 1, status, mines, neighbor_mine, 3, 3)
    assert(hit == False)
    assert(status == [['None', 'None', 'None'],['None', 'Explored', 'None'],['None', 'None', 'Flagged']])
    #   0 1 2
    #0 | | | |
    #1 | |2| |
    #2 | | |F|

    hit = explore_board(2, 0, status, mines, neighbor_mine, 3, 3)
    assert(hit == False)

    hit = explore_board(2, 2, status, mines, neighbor_mine, 3, 3)
    assert(hit == False)
    assert(status == [['None', 'None', 'None'],['Explored', 'Explored', 'None'],['Explored', 'Explored', 'Flagged']])
    #   0 1 2
    #0 | | | |
    #1 |2|2| |
    #2 |0|1|F|

    hit = explore_board(1, 2, status, mines, neighbor_mine, 3, 3)
    assert(hit == False)
    assert(status == [['None', 'None', 'None'],['Explored', 'Explored', 'Explored'],['Explored', 'Explored', 'Flagged']])
    #   0 1 2
    #0 | | | |
    #1 |2|2|2|
    #2 |0|1|F|

    hit = explore_board(2, 2, status, mines, neighbor_mine, 3, 3)
    assert(hit == False)# because it is flagged
    assert(status == [['None', 'None', 'None'],['Explored', 'Explored', 'Explored'],['Explored', 'Explored', 'Flagged']])
    #   0 1 2
    #0 | | | |
    #1 |2|2|2|
    #2 |0|1|F|

    hit = explore_board(0, 1, status, mines, neighbor_mine, 3, 3)
    assert(hit == True)

    hit = explore_board(100, 100, status, mines, neighbor_mine, 3, 3)
    assert(hit == False)

    hit = explore_board(-1, 0, status, mines, neighbor_mine, 3, 3)
    assert(hit == False)


    status = [['None', 'None', 'None', 'None'],['None', 'None', 'None', 'None'],['None', 'None', 'None','None'], ['None', 'None', 'None', 'None']]
    #   0 1 2 3
    #0 | | | | |
    #1 | | | | |
    #2 | | | | |
    #3 | | | | |

    mines = [[False, False, False, True],[False, False, False, True],[False, False, False, False], [False, True, True, False]]
    #   0 1 2 3
    #0 | | | |*|
    #1 | | | |*|
    #2 | | | | |
    #3 | |*|*| |
    neighbor_mine = [[0, 0, 2, 2], [0, 0,2,2], [1,2,3,2], [1,1,1,1]]
    #   0 1 2 3
    #0 |0|0|2|2|
    #1 |0|0|2|2|
    #2 |1|2|3|2|
    #3 |1|1|1|1|
    hit = explore_board(0, 0, status, mines, neighbor_mine, 3, 3)
    assert(hit == False)
    assert(status == [['Explored', 'Explored', 'Explored', 'None'], ['Explored', 'Explored', 'Explored', 'None'], ['Explored', 'Explored', 'Explored', 'None'], ['None', 'None', 'None', 'None']])
    print("Pass all cases!")


