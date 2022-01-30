def has_won(status, width, height, number_of_mines):
    unexplored = 0
    for i in range(height):
        for j in range(width):
            if status[i][j] != 'Explored':
                unexplored += 1

    return unexplored == number_of_mines





#Testing cases.

if __name__ == '__main__': 
    assert(has_won([['None', 'None'], ['None', 'None']], 2, 2, 4) == True)
    assert(has_won([['Explored', 'Explored'], ['Explored', 'Explored']], 2, 2, 0) == True)
    assert(has_won([['Explored', 'Flagged', 'None'], ['None', 'Explored', 'Flagged'], ['None', 'None', 'None']], 3, 3, 0) == False)
    assert(has_won([['Explored', 'Flagged', 'None'], ['None', 'Explored', 'Flagged'], ['None', 'None', 'None']], 3, 3, 1) == False)
    assert(has_won([['Explored', 'Flagged', 'None'], ['None', 'Explored', 'Flagged'], ['None', 'None', 'None']], 3, 3, 2) == False)
    assert(has_won([['Explored', 'Flagged', 'None'], ['None', 'Explored', 'Flagged'], ['None', 'None', 'None']], 3, 3, 3) == False)
    assert(has_won([['Explored', 'Flagged', 'None'], ['None', 'Explored', 'Flagged'], ['None', 'None', 'None']], 3, 3, 4) == False)
    assert(has_won([['Explored', 'Flagged', 'None'], ['None', 'Explored', 'Flagged'], ['None', 'None', 'None']], 3, 3, 5) == False)
    assert(has_won([['Explored', 'Flagged', 'None'], ['None', 'Explored', 'Flagged'], ['None', 'None', 'None']], 3, 3, 6) == False)
    assert(has_won([['Explored', 'Flagged', 'None'], ['None', 'Explored', 'Flagged'], ['None', 'None', 'None']], 3, 3, 7) == True)
    assert(has_won([['Explored', 'Flagged', 'None', 'None'], ['None', 'Explored', 'Flagged', 'None'], ['None', 'None', 'None', 'Flagged']], 4, 3, 10) == True)
    assert(has_won([['Explored', 'Flagged', 'None', 'None'], ['None', 'Explored', 'Flagged', 'None'], ['None', 'None', 'None', 'Flagged']], 4, 3, 9) == False)
    print("Pass all cases!")

