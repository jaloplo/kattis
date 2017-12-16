"""
Solution to the problem Yoda in Kattis web page.
Link: https://open.kattis.com/problems/yoda
"""
import sys

if __name__ == "__main__":
    number1 = sys.stdin.readline().strip()
    number2 = sys.stdin.readline().strip()

    result1 = []
    result2 = []

    if len(number1) > len(number2):
        number2 = number2.zfill(len(number1))
    elif len(number2) > len(number1):
        number1 = number1.zfill(len(number2))

    for i in range(len(number1)):
        if number1[i] > number2[i]:
            result1.append(number1[i])
        elif number2[i] > number1[i]:
            result2.append(number2[i])
        else:
            result1.append(number1[i])
            result2.append(number2[i])

    print 'YODA' if len(result1) == 0 else int(''.join(result1))
    print 'YODA' if len(result2) == 0 else int(''.join(result2))
