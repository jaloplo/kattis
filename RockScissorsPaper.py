"""
Solution to the problem Rock, Scissors, Paper in Kattis web page.
Link: https://open.kattis.com/problems/rockscissorspaper
"""
import sys

if __name__ == "__main__":
    for t in range(int(sys.stdin.readline())):
        rows, columns, days = [int(n) for n in sys.stdin.readline().split()]

        # Board creation
        board = ''
        for r in range(rows):
            board += sys.stdin.readline().strip()

        board_updated = ''
        # Update the whole board
        for day in range(days):

            # Update each cell comparing it with its siblings
            for position, value in enumerate(board):
                siblings = ''
                # Top
                siblings += board[position-columns] if position >= columns else ''
                # Bottom
                siblings += board[position+columns] if position < (columns*(rows-1)) else ''
                # Left
                siblings += board[position-1] if position % columns != 0 else ''
                # Right
                siblings += board[position+1] if position % columns != (columns-1) else ''

                if value == 'P' and 'S' in siblings:
                    board_updated += 'S'
                elif value == 'S' and 'R' in siblings:
                    board_updated += 'R'
                elif value == 'R' and 'P' in siblings:
                    board_updated += 'P'
                else:
                    board_updated += value

            board = board_updated
            board_updated = ''

        for n in range(rows):
            print board[n*columns:n*columns+columns]
