"""
Solution to the problem T9Spelling in Kattis web page.
Link: https://open.kattis.com/problems/t9spelling
"""
import sys

if __name__ == "__main__":
    keypad = {
        'a': '2', 'b': '22', 'c': '222',
        'd': '3', 'e': '33', 'f': '333',
        'g': '4', 'h': '44', 'i': '444',
        'j': '5', 'k': '55', 'l': '555',
        'm': '6', 'n': '66', 'o': '666',
        'p': '7', 'q': '77', 'r': '777', 's': '7777',
        't': '8', 'u': '88', 'v': '888',
        'w': '9', 'x': '99', 'y': '999', 'z': '9999',
        ' ': '0'}
    results = []
    for n in range(int(sys.stdin.readline())):
        results.append('Case #%d: ' % (n+1))
        for c in sys.stdin.readline()[:-1]:
            if results[-1][-1] == keypad[c][0]:
                results[-1] += ' '
            results[-1] += keypad[c]
    for r in results:
        print r.strip()
