"""
Solution to the problem Character Development in Kattis web page.
Link: https://open.kattis.com/problems/character
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
    characters = int(file.readline())
    
    total = 0
    char_fact = math.factorial(characters)
    for g in range(2, characters+1):
        value = char_fact/(math.factorial(characters - g) * math.factorial(g))
        total += value
        #print 'g -> %d  value -> %d  total -> %d' % (g, value, total)

    print total

if __name__ == '__main__':
    solution()

# m! / (m-n)!*n!
# 2! / (2-2)! * 2!
# 3! / (3-2)! * 2 + 3! / (3-3)! * 3!