"""
Solution to the problem Even Up Solitaire in Kattis web page.
Link: https://open.kattis.com/problems/evenup
"""
import sys

def get_source():
    """Set the source as a file readed from the console or
    the user input."""
    if len(sys.argv) > 1:
        return open(sys.argv[1])
    else:
        return sys.stdin

def solution():
    """Solution to the problem."""
    file = get_source()
    total_numbers = int(file.readline())
    even_odds = [int(n) % 2 for n in file.readline().split()]
    counter = [0]
    for i in range(len(even_odds)):
        if i == 0 or even_odds[i] == even_odds[i-1]:
            counter[-1] = counter[-1] + 1
        else:
            counter.append(1)

    ocurrences = [len(n) for n in ''.join(str(n%2) for n in counter).split('0')]
    print abs(sum(o for index, o in enumerate(ocurrences) if index % 2 == 0) - sum(o for index, o in enumerate(ocurrences) if index % 2 == 1))

if __name__ == '__main__':
    solution()
