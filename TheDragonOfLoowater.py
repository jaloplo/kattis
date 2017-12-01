import sys

heads, knights = [(int(i), []) for i in sys.stdin.readline().split(' ')]
while heads[0] != 0 or knights[0] != 0:
    for i in range(heads[0]):
        heads[1].append(int(sys.stdin.readline()))
    heads[1].sort()

    for i in range(knights[0]):
        k = int(sys.stdin.readline())
        if len(heads[1]) > 0 and k >= heads[1][0]:
            knights[1].append(k)
    knights[1].sort()

    money = 0
    if len(heads[1]) > 0:
        for k in range(len(knights[1])):
            if knights[1][k] >= heads[1][0]:
                heads[1].remove(heads[1][0])
                money += knights[1][k]
            if len(heads[1]) == 0:
                print money
                break
        if len(heads[1]) > 0:
            print 'Loowater is doomed!'
    else:
        print 'Loowater is doomed!'

    heads, knights = [(int(i), []) for i in sys.stdin.readline().split(' ')]