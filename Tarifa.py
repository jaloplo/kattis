import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
used = 0
for i in range(n):
    used += int(sys.stdin.readline())

print ((n*x) - used) + x