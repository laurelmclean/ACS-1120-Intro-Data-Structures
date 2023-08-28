import random
import sys

list = sys.argv[1:]

random.shuffle(list)

str = ' '.join(list)

print(str)
