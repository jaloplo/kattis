"""
Solution to the problem Railroad in Kattis web page.
Link: https://open.kattis.com/problems/railroad2
"""
import sys

X_SHAPED_PATHS = 4
Y_SHAPED_PATHS = 3

if __name__ == "__main__":
    x, y = [int(s) for s in sys.stdin.readline().split()]

    print 'possible' if (x * X_SHAPED_PATHS + y * Y_SHAPED_PATHS) % 2 == 0 else 'impossible'
