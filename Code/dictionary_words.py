import random
import sys

number = int(sys.argv[1])

wl = open('/usr/share/dict/words', 'r')
wordlist = wl.read().split()

def random_sentence():
    sentence = random.choices(wordlist, k=number)
    str = ' '.join(sentence)
    print(str)

if __name__ == '__main__':
    sentence = random_sentence()
