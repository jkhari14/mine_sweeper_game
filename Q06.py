def flag_board(i, j, status, width, height):
    if (i < 0 or i >= height or j < 0 or j >= width):
        return
    if (status[i][j] != 'Explored'):
        status[i][j] = 'Flagged'

def unflag_board(i, j, status, width, height):
    if (i < 0 or i >= height or j < 0 or j >= width):
        return
    if (status[i][j] == 'Flagged'):
        status[i][j] = 'None'





#Testing cases.
if __name__ == '__main__':
    status = [['None', 'None', 'None'],['None', 'Explored', 'None'],['None', 'None', 'Flagged']]
    #   0 1 2
    #0 | | | |
    #1 | |1| |
    #2 | | |F|

    flag_board(0, 0, status, 3, 3)
    assert(status == [['Flagged', 'None', 'None'],['None', 'Explored', 'None'],['None', 'None', 'Flagged']])
    #   0 1 2
    #0 |F| | |
    #1 | |1| |
    #2 | | |F|

    flag_board(1, 1, status, 3, 3)
    assert(status == [['Flagged', 'None', 'None'],['None', 'Explored', 'None'],['None', 'None', 'Flagged']])
    #   0 1 2
    #0 |F| | |
    #1 | |1| |
    #2 | | |F|

    flag_board(0, 0, status, 3, 3)
    assert(status == [['Flagged', 'None', 'None'],['None', 'Explored', 'None'],['None', 'None', 'Flagged']])
    #   0 1 2
    #0 |F| | |
    #1 | |1| |
    #2 | | |F|

    flag_board(0, 1, status, 3, 3)
    assert(status == [['Flagged', 'Flagged', 'None'],['None', 'Explored', 'None'],['None', 'None', 'Flagged']])
    #   0 1 2
    #0 |F|F| |
    #1 | |1| |
    #2 | | |F|

    flag_board(2, 1, status, 3, 3)
    assert(status == [['Flagged', 'Flagged', 'None'],['None', 'Explored', 'None'],['None', 'Flagged', 'Flagged']])
    #   0 1 2
    #0 |F|F| |
    #1 | |1| |
    #2 | |F|F|

    unflag_board(2, 2, status, 3, 3)
    assert(status == [['Flagged', 'Flagged', 'None'],['None', 'Explored', 'None'],['None', 'Flagged', 'None']])
    #   0 1 2
    #0 |F|F| |
    #1 | |1| |
    #2 | |F| |

    unflag_board(0, 0, status, 3, 3)
    assert(status == [['None', 'Flagged', 'None'],['None', 'Explored', 'None'],['None', 'Flagged', 'None']])
    #   0 1 2
    #0 | |F| |
    #1 | |1| |
    #2 | |F| |


    unflag_board(1, 1, status, 3, 3)
    assert(status == [['None', 'Flagged', 'None'],['None', 'Explored', 'None'],['None', 'Flagged', 'None']])
    #   0 1 2
    #0 | |F| |
    #1 | |1| |
    #2 | |F| |

    unflag_board(0, 0, status, 3, 3)
    assert(status == [['None', 'Flagged', 'None'],['None', 'Explored', 'None'],['None', 'Flagged', 'None']])
    #   0 1 2
    #0 | |F| |
    #1 | |1| |
    #2 | |F| |
    print("Pass all cases!")
