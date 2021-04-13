import copy, time, sys
from util import parseCommandLine, shapes, string_to_array

class Board:
    def __init__(self, size=10, active_list = None, periodic = True):
        self.size = size
        self.state = [[0 for i in range(size)] for j in range(size)]
        self.periodic = periodic
        if active_list:
            for pair in active_list:
                self.state[pair[0]][pair[1]] = 1

    def update_state(self, i, j, value):
        self.state[i][j]  = value

    def flip_state(self, i, j):
        self.update_state(i,j, 1-self.state[i][j])
    
    def get_neighbours(self, i, j):
        neighbours = []
        for ii in range(3):
            for jj in range(3):
                if self.periodic:
                    x,y = i+ii-1, j+jj-1
                    x = x % self.size
                    y = y % self.size
                    if (x != i or y != j): neighbours.append((x,y))
                else:
                    x,y = i+ii-1,j+jj-1
                    if x >= 0 and x < self.size and y >= 0 and y < self.size and (x != i or y != j):
                        neighbours.append((x,y))
        return neighbours
    
    def count_live_neighbours(self, i, j):
        counter = 0
        for pair in self.get_neighbours(i,j):
            counter += self.state[pair[0]][pair[1]]
        return counter
    
    def next_generation(self):
        new_state = copy.deepcopy(self.state)
        for i in range(self.size):
            for j in range(self.size):
                if self.state[i][j] == 1:
                    if self.count_live_neighbours(i,j) < 2: new_state[i][j] = 0
                    elif self.count_live_neighbours(i,j) > 3: new_state[i][j] = 0
                else:
                    if self.count_live_neighbours(i,j) == 3: new_state[i][j] = 1
        self.state = new_state
    
    def print(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.state[i][j], end = "  ")
            print()
    
    def animate(self, iterations=10, sleep=0.5):
        for i in range(iterations):
            self.print()
            print()
            self.next_generation()
            time.sleep(sleep)

if __name__ == "__main__":
    options = parseCommandLine()
    if type(options.periodic) != type(True): options.periodic = True
    startingshape = shapes[options.startingshape] if options.startingshape in shapes else string_to_array(options.startingshape)
    board = Board(size=options.size, active_list=startingshape, periodic=options.periodic)
    board.animate(iterations=options.iterations)