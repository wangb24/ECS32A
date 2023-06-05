'''counter3.py
Bode W
ECS 32A
Assignment 7 | Part 3

Writing a word counting class and making a wordle.
This part completes the increment_count method and lookup_count method.
'''

# import wordle
import string

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
        print("Word Counter Initialized")


    def get_num_words(self):
        '''This method returns the number of unique words in the dictionary.'''
        return len(self.word_counts)


    def increment_count(self, word: str) -> None:
        '''This method will increment the count of a word in the dictionary.
        If the word is not in the dictionary, it will add it with a count of 1.
        If the word is in the dictionary, it will increment the count by 1.'''
        # # standardize the word
        # word = word.strip(string.punctuation + string.whitespace).lower()  # went too far...
        # Check if the word is in the dictionary
        if word in self.word_counts:
            # Increment the count of the word
            self.word_counts[word] += 1
        elif word == '':
            return
        else:
            # Add the word to the dictionary with a count of 1
            self.word_counts[word] = 1


    # The lookup_count method returns the count of word
    # from the self.word_counts dictionary. If the word
    # is not in the dictionary, it returns 0.
    def lookup_count(self, word: str) -> int:
        '''This method will return the count of a word in the dictionary.'''
        return self.word_counts.get(word,0)

    # The get_top_words method gets the words with the highest
    # counts out of the dictionary.
    #
    # The parameter num indicates how many words to return.
    #
    # The method returns a list of num (count,word) tuples
    # sorted from highest to lowest.
    # def get_top_words(self,num):
    #     return

# The main program
def main():
    '''main program'''

    ## Make a new Count object
    ## the counter object will keep track of
    ## the counts for all the words in the book
    counter = Count()

    ## Test code for Part 3 and 4.
    ## Uncomment for Part 3 and 4.

    counter.increment_count("Well,")
    counter.increment_count("oven")
    counter.increment_count("well")
    counter.increment_count("....'")
    print(counter.lookup_count("oven"))
    print(counter.lookup_count("well"))
    print(counter.lookup_count("pizza"))
    print(counter.lookup_count(""))

    print("Unique words:", counter.get_num_words())
    ## For Part 5 Onward
    ## Open the user specified book file

##        filename = input("Enter book file:")
##        infile = open(filename)

    ## Put a loop here that extracts all words and
    ## inserts each word into the counter object by calling
    ## the counter.increment_count() method

    ## Test code for Part 5 and 6.
    ## Uncomment for Part 5 and 6.
    ## After completing Part 6 remove these lines
##        print("alice:",counter.lookup_count("alice"))
##        print("rabbit:",counter.lookup_count("rabbit"))
##        print("and:",counter.lookup_count("and"))
##        print("she:",counter.lookup_count("she"))
    ## Test code for Part 7. 
    ## Uncomment for Part 7.
##        print("Top 10 Words:")
##        top_ten = counter.get_top_words(10)
##        print(top_ten)

    # print("Unique words:", counter.get_num_words())

    ## Finally, after you have submitted all parts
    ## of the assignment, uncomment the call to the
    ## wordle method below!
    ##
    ## You do not have to submit this part.
    ##
    ## If there is a problem with your Tk installation
    ## the lab computers have been set up to run the code.
    ##
##        wordle.wordleFromObject(counter,30)

# Call the main program
main()
