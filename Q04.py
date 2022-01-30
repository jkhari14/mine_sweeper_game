def compute_neighbor_mine(width, height, mines):
    neighbor_mine = [[0 for j in range(width)] for i in range(height)]
    direction = [0,1, 0,-1, 1,0, -1,0, 1,1, -1,-1, -1,1, 1,-1]
    for i in range(height):
        for j in range(width):        
            for k in range(-1,14,2):
                if i+direction[k+1] >= 0 and i+direction[k+1] < height and j+direction[k+2] >= 0 and j+direction[k+2] < width :
                    if mines[i+direction[k+1]][j+direction[k+2]] == True:
                        neighbor_mine[i][j] += 1
    return neighbor_mine
    






#Testing cases.
if __name__ == '__main__':
    neighbor_mine = compute_neighbor_mine(2, 2, [[False, False],[False, False]])
    assert(neighbor_mine[0][0] == 0)
    assert(neighbor_mine[0][1] == 0)
    assert(neighbor_mine[1][0] == 0)
    assert(neighbor_mine[1][1] == 0)
# status
#   0 1
#0 | | |
#1 | | |

    neighbor_mine = compute_neighbor_mine(2, 2, [[True, True],[True, True]])
    assert(neighbor_mine[0][0] == 3)
    assert(neighbor_mine[0][1] == 3)
    assert(neighbor_mine[1][0] == 3)
    assert(neighbor_mine[1][1] == 3)
#   0 1
#0 |*|*|
#1 |*|*|

    neighbor_mine = compute_neighbor_mine(3, 3, [[True, True, False],[False, True, False],[True, False, False]])
    assert(neighbor_mine[0][0] == 2)
    assert(neighbor_mine[0][1] == 2)
    assert(neighbor_mine[0][2] == 2)
    assert(neighbor_mine[1][0] == 4)
    assert(neighbor_mine[1][1] == 3)
    assert(neighbor_mine[1][2] == 2)
    assert(neighbor_mine[2][0] == 1)
    assert(neighbor_mine[2][1] == 2)
    assert(neighbor_mine[2][2] == 1)
#   0 1 2
#0 |*|*| |
#1 | |*| |
#2 |*| | |

    neighbor_mine=compute_neighbor_mine(4, 3, [[True, True, False, False],[False, True, False, False],[True, False, False, True]])
    assert(neighbor_mine[0][0] == 2)
    assert(neighbor_mine[0][1] == 2)
    assert(neighbor_mine[0][2] == 2)
    assert(neighbor_mine[0][3] == 0)
    assert(neighbor_mine[1][0] == 4)
    assert(neighbor_mine[1][1] == 3)
    assert(neighbor_mine[1][2] == 3)
    assert(neighbor_mine[1][3] == 1)
    assert(neighbor_mine[2][0] == 1)
    assert(neighbor_mine[2][1] == 2)
    assert(neighbor_mine[2][2] == 2)
    assert(neighbor_mine[2][3] == 0)
#   0 1 2 3
#0 |*|*| | |
#1 | |*| | |
#2 |*| | |*|

    neighbor_mine=compute_neighbor_mine(4, 3, [[True, True, True, False],[False, True, False, True],[True, False, False, True]])
    assert(neighbor_mine[0][0] == 2)
    assert(neighbor_mine[0][1] == 3)
    assert(neighbor_mine[0][2] == 3)
    assert(neighbor_mine[0][3] == 2)
    assert(neighbor_mine[1][0] == 4)
    assert(neighbor_mine[1][1] == 4)
    assert(neighbor_mine[1][2] == 5)
    assert(neighbor_mine[1][3] == 2)
    assert(neighbor_mine[2][0] == 1)
    assert(neighbor_mine[2][1] == 2)
    assert(neighbor_mine[2][2] == 3)
    assert(neighbor_mine[2][3] == 1)
#   0 1 2 3
#0 |*|*|*| |
#1 | |*| |*|
#2 |*| | |*|

    print("Pass all cases!")

