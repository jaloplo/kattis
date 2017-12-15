"""
Solution to the problem Left Beehind in Kattis web page.
Link: https://open.kattis.com/problems/leftbeehind
"""
import sys

if __name__ == "__main__":
    results = []
    sweet, sour = [int(n) for n in sys.stdin.readline().split()]
    while sweet != 0 or sour != 0:
        delta = sweet - sour
        if sweet + sour == 13:
            results.append('Never speak again.')
        elif delta == 0:
            results.append('Undecided.')
        elif delta < 0:
            results.append('Left beehind.')
        else:
            results.append('To the convention.')
        sweet, sour = [int(n) for n in sys.stdin.readline().split()]

    for r in results:
        print r
