'''moving_ave_csv.py
Bode W
Homework 5 | Problem 6

This program will do everything that moving_ave.py does, but it will
write the output to a csv file instead of printing it to the terminal.
'''

# run the moving_ave.py program
import moving_ave

# store each line of the output in a list of strings
contents = []
for yrs, avg in zip(moving_ave.c_year, moving_ave.average):
    contents.append(f"{yrs},{avg:.4f}")

# write the outputs to a csv file
with open('MovingAve.csv', 'w', encoding='utf-8') as file:
    file.write("Year,Value\n")  # write the header
    file.write('\n'.join(contents))  # write the contents
