"""
Solution to the problem Sibice in Kattis web page.
Link: https://open.kattis.com/problems/sibice
"""
import math
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
    n, w, h = [int(s) for s in file.readline().split()]
    longest = int(math.sqrt(pow(w, 2) + pow(h, 2)))
    matches = []
    for i in range(n):
        matches.append(int(file.readline()))
    for match in matches:
        print 'DA' if longest >= match else 'NE'

if __name__ == '__main__':
    solution()
