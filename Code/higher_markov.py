import random
import re

class HigherMarkovChain():
    def __init__(self, source_text):
        self.words_list = self.clean_text(source_text)
        self.markov_chain = {}
        self.random_sentence = []

    def clean_text(self, source_text):
        # Replace special characters and convert ’ to '
        cleaned_text = source_text.replace("’", "'")
        # Remove numbers and underscores
        cleaned_text = re.sub(r"[0-9_]+", "", cleaned_text)
        # Extract words using regex
        word_list = [match.group() for match in re.finditer(r"[a-zA-Z0-9_'.:,-;!?]+", cleaned_text)]
        return word_list

    def create_markov_chain(self):
        window_size = 2 

        # Loop through the words in the source text
        for i in range(len(self.words_list) - window_size):
            # Create a tuple as a sliding window
            window = tuple(self.words_list[i:i + window_size])
            next_word = self.words_list[i + window_size]

            # If the window is not in the Markov chain, add it as a key
            if window not in self.markov_chain:
                self.markov_chain[window] = {}

            # If the next word is not in the window's dictionary, add it with a frequency of 0
            if next_word not in self.markov_chain[window]:
                self.markov_chain[window][next_word] = 0

            # Increment the frequency of the next word in the window's dictionary
            self.markov_chain[window][next_word] += 1

    def generate_sentence(self):
        # Start with a random tuple
        current_tuple = random.choice(list(self.markov_chain.keys()))
        # Add the tuple to the sentence
        self.random_sentence.extend(current_tuple)
         # Determine the length of the sentence randomly
        word_count = random.randint(10, 25)

        for _ in range(word_count):
            # Get the dictionary for the current tuple
            nested_dict = self.markov_chain.get(current_tuple)

            if nested_dict:
                words = list(nested_dict.keys())
                weights = list(nested_dict.values())
                 # Choose the next word based on its frequency in the dictionary
                next_word = random.choices(words, weights)[0]
                self.random_sentence.append(next_word)
                # Update the current tuple by removing the first word and adding the next word
                current_tuple = current_tuple[1:] + (next_word,)
        
        # Generate random end punctuation
        end_punctuation = ['.', '!', '?', '...']
        random_end_punctuation = random.choice(end_punctuation)

        self.random_sentence = " ".join(self.random_sentence).capitalize() + random_end_punctuation

def main():
    text_file = 'alice.txt'
    source_text = open(text_file, "r").read()
    chain = HigherMarkovChain(source_text)
    chain.create_markov_chain()
    chain.generate_sentence()
    return chain.random_sentence

if __name__ == '__main__':
    main()
