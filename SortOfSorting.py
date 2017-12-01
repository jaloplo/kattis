"""
Solution to the problem Sort of Sorting in Kattis web page.
Link: https://open.kattis.com/problems/sortofsorting
"""
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    names = []
    while n:
        if len(names) > 0:
            names.append('')

        test_case_names = []
        for i in range(n):
            test_case_names.append(sys.stdin.readline().strip())
        names.extend(sorted(test_case_names, key=lambda name: name[0:2]))

        n = int(sys.stdin.readline())
    
    for name in names:
        print name
