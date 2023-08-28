import random
import sys

def histogram(filename):
    book = open(filename, "r").read().lower()
    wordlist = book.split()
    histogram = dict()
    for i in wordlist:
        histogram[i] = histogram.get(i, 0) + 1
    print(histogram)
    return histogram


if __name__ == '__main__':
    sentence = histogram("alice.txt")
