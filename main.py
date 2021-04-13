import sys
from util import parseCommandLine, shapes, string_to_array
from board import Board

if __name__ == "__main__":
    options = parseCommandLine()
    if type(options.periodic) != type(True): options.periodic = True
    startingshape = shapes[options.startingshape] if options.startingshape in shapes else string_to_array(options.startingshape)
    board = Board(size=options.size, active_list=startingshape, periodic=options.periodic)
    board.animate(iterations=options.iterations)