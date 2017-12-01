"""
Solution to the problem Aaah! in Kattis web page.
Link: https://open.kattis.com/problems/aaah
"""
import sys

if __name__ == "__main__":
    marius = sys.stdin.readline().strip()
    doctor = sys.stdin.readline().strip()

    if len(marius) >= len(doctor):
        print 'go'
    else:
        print 'no'
