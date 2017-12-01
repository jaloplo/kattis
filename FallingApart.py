import math, sys

numbers = float(sys.stdin.readline())
integers = [int(i) for i in sys.stdin.readline().split(' ')]
integers.sort(reverse=True)
odds = int(math.ceil(numbers/2))
evens = int(math.floor(numbers/2))

alice = 0
bob = 0
for i in range(evens):
    alice += integers[2*i]
    bob += integers[(2*i)+1]
if odds > evens:
    alice += integers[-1]

print alice, bob