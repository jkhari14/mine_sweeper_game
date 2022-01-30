import random

class intPair:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def intPairEqual(ip1, ip2):
    return ip1.x == ip2.x and ip1.y == ip2.y

class hashT:
	def __init__(self) -> None:
		self.hash = {}

	def insert(self, key, val):
		self.hash[key] = val

	def get(self, key):
		try:
			return self.hash[key]
		except KeyError:
			return None


def initialize_board(width, height, number_of_mines):
    status = [['None' for j in range(width)] for i in range(height)]
    mines = [[False for j in range(width)] for i in range(height)]
    placedHash = hashT()
    placedMines = 0
    while placedMines < number_of_mines:
        coordinate = intPair(random.randint(0, height-1), random.randint(0, width-1))
        if placedHash.get(coordinate) != coordinate:
            mines[coordinate.x][coordinate.y] = True
            placedHash.insert(coordinate, coordinate)
            placedMines += 1
    return (mines,status)

            








## testing code
def count_nested_list(input_list, value, width, height):
    return sum([input_list[i][j] == value for i in range(height) for j in range(width)])

if __name__ == '__main__':
    mines, status = initialize_board(2, 2, 1)
    assert(count_nested_list(status, 'None', 2, 2) == 2*2)
    assert(count_nested_list(mines, True, 2, 2) == 1)
    assert(count_nested_list(mines, False, 2, 2) == 2*2-1)

    mines, status = initialize_board(2, 2, 4)
    assert(count_nested_list(status, 'None', 2, 2) == 2*2)
    assert(count_nested_list(mines, True, 2, 2) == 4)
    assert(count_nested_list(mines, False, 2, 2) == 0)

    mines, status = initialize_board(10, 10, 10)
    assert(count_nested_list(status, 'None', 10, 10) == 10*10)
    assert(count_nested_list(mines, True, 10, 10) == 10)
    assert(count_nested_list(mines, False, 10, 10) == 10*10-10)

    mines, status = initialize_board(4, 3, 10)
    assert(count_nested_list(status, 'None', 4, 3) == 4*3)
    assert(count_nested_list(mines, True, 4, 3) == 10)
    assert(count_nested_list(mines, False, 4, 3) == 4*3-10)
    ##changing one cell shouldn't impact other cell
    status[0][0]='Explored'
    assert(status[1][0]=='None')
    

    print("Pass all cases!")
