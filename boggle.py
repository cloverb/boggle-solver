import os
from board import Board
from solver import Solver
from error import InvalidBoardError


def pint_instructions():
    print('You can exit at anytime by pressing ctrl-c or typing exit')
    print('Enter a filename of a text (.txt) file representing a boggle board')
    print('The file must contain lines of English letters separated by a single space')
    print('Example:')
    print('c a t a')
    print('l t o o')
    print('i c k w')
    print('r a s a')


def run():
    print('Initializing dictionary...')
    solver = Solver()
    pint_instructions()
    while True:
        file = input('>>')
        if file == 'exit':
            exit()
        if not os.path.isfile(file):
            print('Invalid file path')
            continue
        try:
            board = Board(file)
            words = solver.solve(board)
            print('{} words found'.format(len(words)))
            if words:
                print(words)
        except InvalidBoardError:
            print('Invalid board')
            pint_instructions()


run()
