"""
Solution to the problem Lemonade Trade in Kattis web page.
Link: https://open.kattis.com/problems/lemonadetrade
"""
import math
import sys

def getfile():
    if len(sys.argv) > 0:
        return open(sys.argv[1])
    else:
        sys.stdin

def get_trade(name, trades):
    if not name in trades:
        trades[name] = float('-inf')
    return trades[name]

if __name__ == '__main__':
    file = getfile()
    n = int(file.readline())
    trades = {'pink': math.log(1.0)}
    for i in range(n):
        target, source, weight = file.readline().split(' ')
        value = max(get_trade(target, trades), get_trade(source, trades) + math.log(float(weight)))
        trades[target] = value

    blue = get_trade('blue', trades)
    print 10.0 if blue > math.log(10) else math.exp(blue)
