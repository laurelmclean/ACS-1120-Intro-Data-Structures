import string

def histogram(filename):
    # Load the text from the file and convert to lowercase
    with open(filename, "r") as file:
        book = file.read().lower()

    # Create a translation table to remove punctuation
    translator = str.maketrans("", "", string.punctuation)

    # Remove punctuation from words and split into a list
    wordlist = book.translate(translator).split()
    histogram = dict()
    for i in wordlist:
        histogram[i] = histogram.get(i, 0) + 1
    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram[word]

if __name__ == '__main__':
    alice_histogram = histogram("alice.txt")
    print(alice_histogram)
    length = unique_words(alice_histogram)
    print(length)
    frequency_word = frequency('her', alice_histogram)
    print(frequency_word)
