'''quiz_part2.py
Bode W
Homework 2 | Part 2

The code would ask user 5 questions and then print the results.
'''

## Define a function to ask a question
def ask_question(prompt: str, correct_answer: str) -> None:
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
    else:
        print(f'The correct answer was {correct_answer}')

## Ask the user 5 questions
ask_question('''ART: Who painted 'The Persistance of Memory'?
a. Dali
b. Munch
c. Picasso''', 'a')

ask_question('''ENTERTAINMENT: How many oscars did Hitchcock win?
a. None
b. One
c. Two''', 'a')

ask_question('''SCIENCE: Which dinosaur is most closely related to the pelican?
a. Velociraptor
b. Stegosaurus
c. Pterodactyl''', 'a')

ask_question('''HISTORY: Which of the following was not invented in Baja California?
a. Margaritas
b. Chocolate
c. Caesar Salad''', 'b')

ask_question('''SCIENCE AND NATURE: Can pigs swim?
a. Yes
b. No
c. Only in salt water''', 'a')

ask_question('''SPORT AND LEISURE: What color is the middle Olympic ring?
a. Red
b. Blue
c. Black''', 'c')
