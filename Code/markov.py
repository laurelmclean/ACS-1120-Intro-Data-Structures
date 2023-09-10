from __future__ import division, print_function
import string
from listogram import Listogram

class MarkovChain(dict):
    """MarkovChain represents a Markov chain implemented as a subclass of the dict type."""
    
    def __init__(self, word_list=None):
        """Initialize the Markov chain"""
        super(MarkovChain, self).__init__()
        self.types = 0  # Count of distinct word types in this Markov chain
        # Learn from the given word list, if any
        if word_list is not None:
            self.learn(word_list)

    def learn(self, word_list):
        """Learn from the given text by building the Markov Chain by examining pairs of adjacent words."""
        # iterates through the word_list, which is a list of words or tokens from the input text. 
        # The loop goes up to the second-to-last word in the list because it considers pairs of words to build the Markov chain
        for i in range(len(word_list) - 1):
            # assign the current word
            current_word = word_list[i]
            #  assign next word
            next_word = word_list[i + 1]
            if current_word in self:
                self[current_word].add_count(next_word)
            else:
                #  track frequency of next word following current word
                self[current_word] = Listogram([next_word])
                self.types += 1

    def generate_sentence(self, start_word, num_words):
        """Perform a random walk on this Markov chain starting from the specified word."""
        #  initialize a list with the start word to make the generated sentence
        sentence = [start_word]
        # iterate desired list for generated sentence
        for word in range(num_words - 1):
            #  get last word in walk list
            current_word = sentence[-1]
            # Check if the current_word is a key in the MarkovChain object (self)
            # If it is, it means there are words that can follow the current_word
            if current_word in self:
                #  randomly select the next word based on the probabilities associated with words that can follow current_word in the chain
                next_word = self[current_word].sample()
                #  add next word to the list
                sentence.append(next_word)
            else:
                break
        capitalized = [sentence[0].capitalize()] + sentence[1:]
        print(f"{' '.join(capitalized)}.")
        return capitalized

def main():
    text_file = 'alice.txt'
    source_text = open(text_file, "r").read()
    translator = str.maketrans("", "", string.punctuation + "“”‘’")
    # remove punctuation and split into words
    word_list = source_text.translate(translator).lower().split()
    chain = MarkovChain(word_list)
    start_word = 'the'
    num_words = 15
    chain.generate_sentence(start_word, num_words)
    
if __name__ == '__main__':
    main()