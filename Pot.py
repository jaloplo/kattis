"""
Solution to the problem Pot in Kattis web page.
Link: https://open.kattis.com/problems/pot
"""
import sys

if __name__ == "__main__":
    total = 0
    for n in range(int(sys.stdin.readline())):
        number_as_text = sys.stdin.readline().strip()
        number = int(number_as_text[:-1])
        power = int(number_as_text[-1])
        total += pow(number, power)

    print total
