"""
Solution to the problem Above Average in Kattis web page.
Link: https://open.kattis.com/problems/aboveaverage
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
    results = []
    for c in range(int(file.readline())):
        grades = sorted([int(v) for v in file.readline().split()][1:])
        average = float(sum(grades))/len(grades)
        first = next((i for i,g in enumerate(grades) if g > average), len(grades))
        people_above_average = len(grades) - first
        results.append(people_above_average * 100.0 / len(grades))
    for r in results:
        print '%.3f%%' % r

if __name__ == '__main__':
    solution()
