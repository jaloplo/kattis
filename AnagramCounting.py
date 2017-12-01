"""
Solution to the problem Anagram Counting in Kattis web page.
Link: https://open.kattis.com/problems/anagramcounting
"""
import math
import sys

if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    factors = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    solutions = []
    while len(line):
        fact = math.factorial(len(line))
        times = [line.count(n) for n in set(line) if line.count(n) > 1]
        repeated = len(line) - len(set(line)) - len(times)
        divisor = 1
        for t in times:
            for f in range(0, t-1):
                divisor *= factors[f]
        solutions.append(fact/divisor)
        line = sys.stdin.readline().strip()
    for s in solutions:
        print s
