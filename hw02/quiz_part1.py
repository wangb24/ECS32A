'''quiz_part1.py
Bode W
Homework 2 | Part 1

The code would ask a question and then ask the user for their answer.
Then it would print if the answer was correct or not.
'''

## Print the question to the terminal
print('''ART: Who painted 'The Persistance of Memory'?
a. Dali
b. Munch
c. Picasso''')

## Then ask the user for their answer
user_answer = input('Enter your choice:')

## The following code prints the result
if user_answer.lower().strip() == 'a':
    print('Correct!')
else:
    print('The correct answer was a')
