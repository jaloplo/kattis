"""
Solution to the problem Rock, Scissors, Paper in Kattis web page.
Link: https://open.kattis.com/problems/rockscissorspaper
"""
import sys
import time

TOP = 0
BOTTOM = 1
LEFT = 2
RIGHT = 3

P = 2
R = 3
S = 5

def get_source():
    """Set the source as a file readed from the console or
    the user input."""
    if len(sys.argv) > 1:
        return open(sys.argv[1])
    else:
        return sys.stdin

def transform(character):
    return P if character == 'P' else R if character == 'R' else S

def resolve(value):
    return 'P' if value == P else 'S' if value == S else 'R'

if __name__ == "__main__":
    #start_time = time.time()
    source = get_source()
    for t in range(int(source.readline())):
        rows, columns, days = [int(n) for n in source.readline().split()]

        # Board creation
        board = [[]]
        for r in range(rows):
            for c in source.readline().strip():
                board[-1].append(transform(c))

        siblings = []
        # Calculate siblings
        for position, value in enumerate(board[-1]):
            siblings.append([])
            # Top
            siblings[position].append(position-columns if position >= columns else position)
            # Bottom
            siblings[position].append(position+columns if position < columns*(rows-1) else position)
            # Left
            siblings[position].append(position-1 if position % columns != 0 else position)
            # Right
            siblings[position].append(position+1 if position % columns != columns-1 else position)

        #process_time = time.time()
        # Update the whole board
        for day in range(days):
            board.append([])

            # Update each cell comparing it with its siblings
            for position, value in enumerate(board[-2]):
                s = 1
                s *= board[-2][siblings[position][TOP]]
                s *= board[-2][siblings[position][BOTTOM]]
                s *= board[-2][siblings[position][LEFT]]
                s *= board[-2][siblings[position][RIGHT]]

                if value == P and s % S == 0:
                    board[-1].append(S)
                elif value == S and s % R == 0:
                    board[-1].append(R)
                elif value == R and s % P == 0:
                    board[-1].append(P)
                else:
                    board[-1].append(value)

        #print 'Process time: %s' % (time.time() - process_time)

        solution = ''.join([resolve(i) for i in board[-1]])
        for n in range(rows):
            print solution[n*columns:n*columns+columns]

    #print 'Time: %s' % (time.time() - start_time)
