"""
Solution to the problem Modulo in Kattis web page.
Link: https://open.kattis.com/problems/modulo
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
    modulos = []
    for i in range(10):
        modulos.append(int(file.readline()) % 42)
    print len(set(modulos))

if __name__ == '__main__':
    solution()
