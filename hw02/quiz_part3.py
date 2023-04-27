'''quiz_part3.py
Bode W
Homework 2 | Part 3

The code would ask user 5 questions and then print the results.
It also counts number of correct answers and prints the score.
'''

## Initiate constants and variables
score = 0 # The score of the user
QUESTIONS = [
    '''ART: Who painted 'The Persistance of Memory'?
a. Dali
b. Munch
c. Picasso''',
    '''ENTERTAINMENT: How many oscars did Hitchcock win?
a. None
b. One
c. Two''',
    '''SCIENCE: Which dinosaur is most closely related to the pelican?
a. Velociraptor
b. Stegosaurus
c. Pterodactyl''',
    '''HISTORY: Which of the following was not invented in Baja California?
a. Margaritas
b. Chocolate
c. Caesar Salad''',
    '''SCIENCE AND NATURE: Can pigs swim?
a. Yes
b. No
c. Only in salt water''',
    '''SPORT AND LEISURE: What color is the middle Olympic ring?
a. Red
b. Blue
c. Black'''
] # The questions to ask the user
CORRECT_ANSWERS = ['a', 'a', 'a', 'b', 'a', 'c'] # The correct answers to the questions

## Define a function to ask a question
def ask_question(prompt: str, correct_answer: str) -> bool:
    """Ask the user a question and print the result.

    Args:
        prompt (str): The question to ask the user.
        correct_answer (str): The correct answer to the question.
    """
    # init
    correct_answer = correct_answer.lower().strip()
    # Print the question to the terminal
    print(prompt)

    # Then ask the user for their answer
    user_answer = input('Enter your choice:')

    # The following code prints the result
    if user_answer.lower().strip() == correct_answer:
        print('Correct!')
        return True
    else:
        print(f'The correct answer was {correct_answer}')
        return False


## Ask the user 5 questions
for i, j in zip(QUESTIONS, CORRECT_ANSWERS):
    score = score + int(ask_question(i, j))

## Print the score
print(f'Your total score is {score}')
