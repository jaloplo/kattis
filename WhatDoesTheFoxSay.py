import sys

t = int(sys.stdin.readline())
words = []
for i in range(t):
    words = [i.strip() for i in sys.stdin.readline().split(' ')]

    animal = sys.stdin.readline().split(' goes ')
    while animal[0].strip() != 'what does the fox say?':
        sound = animal[1].strip()
        while words.count(sound):
            words.remove(sound)
        animal = sys.stdin.readline().split(' goes ')

    fox_sound = ''
    for w in words:
        fox_sound += w + ' '
    print fox_sound.strip()