from optparse import OptionParser
import ast

def parseCommandLine():
    usageStr = "A simple Python implementation of Conway's game of life"
    parser = OptionParser(usageStr)
    parser.add_option('-s', '--size', dest='size', help='The n x n size of the board. Can be periodic', type='int', default=10)
    parser.add_option('-g', '--startingshape', dest='startingshape', help='the starting shape on the board. e.g. glider, block, oscillator, [(1,0),(1,1),(1,2)]', default='glider')
    parser.add_option('-p', '--periodic', action="store_true", dest='periodic', help='Whether the board is bounded or periodic (infinite)')
    parser.add_option('-b', '--bounded', action="store_false", dest='periodic', help='Whether the board is bounded or periodic (infinite)')
    parser.add_option('-n', '--iterations', dest='iterations', help='Number of generations (animation frames) for the game of life', type='int', default=20)
    options, rest_of_command = parser.parse_args()
    if len(rest_of_command) != 0: raise Exception('Command line input not understood: ' + str(rest_of_command))
    return options

def string_to_array(str):
    return ast.literal_eval(str)

shapes = {
    'glider': [(2,0),(2,1),(2,2),(1,2),(0,1)],
    'block': [(0,0),(1,0),(0,1),(1,1)],
    'oscillator': [(1,0),(1,1),(1,2)]
}
