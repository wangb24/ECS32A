'''counter.py
Bode W
ECS 32A
Assignment 7

Writing a word counting class and making a wordle.
'''

import wordle
import string

IGNORED_WORDS_PATH = 'data/stop_words.txt'

#
# The Count class
#
# The class keyword below begins the definition of a new Python data type Count.
# Count keeps word counts. All the methods that we can use with Count objects
# and the variables (attributes) built inside Count objects are defined in the
# this class definition.
#
class Count:
    '''This class keeps track of word counts.
    When an instance of this class is created, a dictionary named word_counts
    is created to hold the counts for each word. The keys of the dictionary
    are the words and the values are the counts.
    
    The methods in this class are:
        __init__ - initializes the word_counts dictionary
        get_num_words - returns the number of unique words in the dictionary
        increment_count - increments the count of a word in the dictionary
        lookup_count - returns the count of a word in the dictionary
    '''

    def __init__(self):
        # Initialize word_counts to an empty dictionary
        self.word_counts = {}
        self.ignored_words = set()
        with open(IGNORED_WORDS_PATH, mode='r', encoding='utf-8') as file:
            words = file.read().lower().split()
            [self.ignored_words.add(word) for word in words]
        print("Word Counter Initialized")


    def __str__(self):
        # Return a string showing number of unique words
        return f"Unique words: {self.get_num_words()}"


    def get_num_words(self):
        '''This method returns the number of unique words in the dictionary.'''
        return len(self.word_counts)


    def increment_count(self, word: str) -> None:
        '''
        This method will increment the count of a word in the dictionary.
        If the word is not in the dictionary, it will add it with a count of 1.
        If the word is in the dictionary, it will increment the count by 1.'''
        # standardize the word
        word = word.strip(string.punctuation + string.whitespace).lower()
        # Check if the word is in the dictionary
        if word in self.word_counts:
            # Increment the count of the word
            self.word_counts[word] += 1
        elif word == '' or word in self.ignored_words:
            return
        else:
            # Add the word to the dictionary with a count of 1
            self.word_counts[word] = 1


    def lookup_count(self, word: str) -> int:
        '''
        This method will return the count of a word in the dictionary,
        or 0 if the word is not in the dictionary.'''
        return self.word_counts.get(word, 0)


    def get_top_words(self, num: int) -> list:
        '''
        This method will return a list of (count,word) tuples of the
        num most frequent words in the dictionary.'''
        # Sort the words in the dictionary by count
        sorted_words = sorted(self.word_counts.items(), key=lambda x: x[1], reverse = True)
        # Flip the order of the (word,count) tuples
        sorted_words = [(count, word) for word, count in sorted_words]
        # Return the top num words
        return sorted_words[:num]

# The main program
def main():
    '''main program'''

    ## Make a new Count object
    ## the counter object will keep track of
    ## the counts for all the words in the book
    counter = Count()


    ## Open the user specified book file
    filename = input("Enter book file:")
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            if line == '\n':
                continue
            for word in line.split():
                # This for loop extracts each word from the line
                # and inserts it into the counter object with method
                # `increment_count`
                counter.increment_count(word)

    ## Finally, after you have submitted all parts
    ## of the assignment, uncomment the call to the
    ## wordle method below!
    ##
    ## You do not have to submit this part.
    ##
    ## If there is a problem with your Tk installation
    ## the lab computers have been set up to run the code.
    ##
    wordle.wordleFromObject(counter,30)

# Call the main program
main()
