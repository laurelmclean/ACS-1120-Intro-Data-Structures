import string
import random

def histogram(filename):
    # Load the text from the file and convert to lowercase
    with open(filename, "r") as file:
        book = file.read().lower()

    # Create a translation table to remove punctuation
    translator = str.maketrans("", "", string.punctuation + "“”‘’")

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


def stochastic_sampling(histogram):
    words = list(histogram.keys())
    probabilities = list(histogram.values())
    total_probability = sum(probabilities)
    normalized_probabilities = []
    for i in probabilities:
        normalized_probabilities.append(i / total_probability)
    word = random.choices(words, weights=normalized_probabilities, k=1)[0]
    return word

def main():
    hist = histogram("alice.txt")
    length = random.randint(1, 15)
    selected_words = [stochastic_sampling(hist) for word in range(length)]
    selected_words[0] = selected_words[0].capitalize()
    random_sentence = " ".join(selected_words)
    return random_sentence

if __name__ == '__main__':
    alice_histogram = histogram("alice.txt")
    print(alice_histogram)
    length = unique_words(alice_histogram)
    print(length)
    frequency_word = frequency('her', alice_histogram)
    print(frequency_word)
    print(stochastic_sampling(alice_histogram))
    print(main())
