import sys

line = sys.stdin.readline().strip()
while len(line) > 0:
    numbers = [int(i) for i in line.split(' ')]
    print sum(numbers)/2
    line = sys.stdin.readline().strip()