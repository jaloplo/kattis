"""
Solution to the problem Paradox With Averages (Hard) in Kattis web page.
Link: https://open.kattis.com/problems/averageshard
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
    test_cases = int(file.readline())
    for test in range(test_cases):
        file.readline()
        number_students_cs, number_students_e = [int(i) for i in file.readline().split()]
        students_cs = [int(i) for i in file.readline().split()]
        students_e = [int(i) for i in file.readline().split()]

        average_cs = sum(students_cs)/float(number_students_cs)
        average_e = sum(students_e)/float(number_students_e)

        print len([s for s in students_cs if s > average_e and s < average_cs])

if __name__ == '__main__':
    solution()
