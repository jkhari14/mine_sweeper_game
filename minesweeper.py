#IMPORANT: DO NOT CHANGE code in this file except for the final line of code!
from Q01 import print_status
from Q02 import print_mine
from Q03 import initialize_board
from Q04 import compute_neighbor_mine
from Q05 import explore_board
from Q06 import flag_board, unflag_board
from Q07 import has_won

#This is a function that clear the screen when running the code in a terminal
def clear_screen(): 
    from os import system, name 
    system('cls' if name == 'nt' else 'clear')

#This function is to initiate the size and number of mines for the game.
def start_game(width, height, number_of_mines):
    mines, status = initialize_board(width, height, number_of_mines)
    neighbor_mine = compute_neighbor_mine(width, height, mines)
    while True:
        clear_screen()
        print_status(width, height, status, neighbor_mine)
        s = input("Enter operation: op x y:").split()
        if s[0].upper() == 'E':
            hit = explore_board(int(s[1]), int(s[2]), status, mines, neighbor_mine, width, height)
            if hit:
                print("Boom! You lost! Mine pattern:")
                print_mine(width, height,mines)
                return
            else:
                if has_won(status, width, height, number_of_mines):
                    print("You win!! Mine pattern:")
                    print_mine(width, height,mines)
                    return       
        elif s[0].upper() == 'F':
            flag_board(int(s[1]), int(s[2]), status, width, height)
        elif s[0].upper() == 'U':
            unflag_board(int(s[1]), int(s[2]), status, width, height)



#initiate size and number of mines and start the game!
start_game(10, 10, 10)
