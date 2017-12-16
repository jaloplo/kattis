"""
Solution to the problem Pig Latin in Kattis web page.
Link: https://open.kattis.com/problems/piglatin
"""
import sys

CONSONANTS = 'bcdfghjklmnpqrstvwxz'
VOWELS = 'aeiouy'

if __name__ == "__main__":
    piglatin = []

    phrase = sys.stdin.readline().strip()
    while phrase != '':
        piglatin.append([])
        for word in phrase.split():
            if word[0] in VOWELS:
                piglatin[-1].append(''.join([word, 'yay']))
            else:
                index = word.replace('a', ' ').replace('e', ' ').replace('i', ' ').replace('o', ' ').replace('u', ' ').replace('y', ' ').find(' ')
                piglatin[-1].append(''.join([word[index:], word[0:index], 'ay']))
        phrase = sys.stdin.readline().strip()

    for p in piglatin:
        print ' '.join(p)
