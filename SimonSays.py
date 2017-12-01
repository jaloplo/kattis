import sys

t = int(sys.stdin.readline())
for i in range(t):
    line = sys.stdin.readline().strip().split('simon says ')
    if len(line) > 1:
        print line[1].strip()