'''translate.py
Bode W
Homework 4 | Problem 5

Ask user to input a word.
If the word starts with a vowel, add "way" to the end of the word.
Otherwise, move the first letter to the end of the word and add "ay" to the end.
Finally, print out the translated word.
'''

# ask user to input a word
user_input = input("Enter a word:").lower()

# translate the word
if user_input[0] in "aeiou":
    translated = user_input + "way"
else:
    translated = user_input[1:] + user_input[0] + "ay"

# print out the translated word
print(f"{user_input} in Pig latin is {translated}")