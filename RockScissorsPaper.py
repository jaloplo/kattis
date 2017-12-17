"""
Solution to the problem Rock, Scissors, Paper in Kattis web page.
Link: https://open.kattis.com/problems/rockscissorspaper
"""
import sys

def win(source, target):
    return source == 'P' and target == 'R' or source == 'R' and target == 'S' or source == 'S' and target == 'P'

if __name__ == "__main__":
    for t in range(int(sys.stdin.readline())):
        rows, columns, days = [int(n) for n in sys.stdin.readline().split()]

        # Board creation
        board = []
        for r in range(rows):
            board.append(sys.stdin.readline().strip())

        board_updated = []
        # Update the whole board
        for day in range(days):

            # Update each cell comparing it with its siblings
            for x, row in enumerate(board):
                board_updated.append('')
                for y, cell in enumerate(row):
                    if x > 0 and win(board[x-1][y], cell):
                        board_updated[-1] += board[x-1][y]
                        continue

                    if x < rows-1 and win(board[x+1][y], cell):
                        board_updated[-1] += board[x+1][y]
                        continue

                    if y > 0 and win(board[x][y-1], cell):
                        board_updated[-1] += board[x][y-1]
                        continue

                    if y < columns-1 and win(board[x][y+1], cell):
                        board_updated[-1] += board[x][y+1]
                        continue

                    board_updated[-1] += cell

            board = board_updated[:]
            board_updated = []

        for row in board:
            print row
