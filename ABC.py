"""
Solution to the problem ABC in Kattis web page.
Link: https://open.kattis.com/problems/abc
"""
import sys

if __name__ == "__main__":
    numbers = sorted([int(n) for n in sys.stdin.readline().strip().split(' ')])
    order = sys.stdin.readline()
    print numbers[ord(order[0])-65], numbers[ord(order[1])-65], numbers[ord(order[2])-65]
