"""
Write a program to return the correct letter grade
"""
from tkinter import messagebox, simpledialog, Tk

# The teacher wants you to write a program that converts the score on 2
# 100 point tests to a letter grade. The teacher wants you to average the
# score from the 2 tests and print out the letter grade back to the user.
# The letter grades are assigned as follows:
#   A = 89.5 to 100
#   B = 79.5 to less than 89.5
#   C = 69.5 to less than 79.5
#   D = 59.5 to less than 69.5
#   F = less than 59.5
if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    # TODO) Ask the user for their score on the FIRST test and store their
    #  score in a variable
    score = simpledialog.askinteger(title = 'test score', prompt = 'What was your score on your first test?')
    score_two= simpledialog.askinteger(title = 'test score', prompt = 'what was your score on the second test?')
    add_score = (score + score_two)/2
    if add_score >=89.5 and add_score<=100.0:
        messagebox.showinfo(title = 'Test Score',message= "You got an A! You must have studied hard!")
    if add_score >=79.5 and add_score<89.5:
        messagebox.showinfo(title = 'Test Score',message= "You got a B! You did Great!")
    if add_score >=69.5 and add_score<79.5:
        messagebox.showinfo(title = 'Test Score',message= "You got an C! Maybe study a little harder?")
    if add_score >=59.5 and add_score<69.5:
        messagebox.showinfo(title = 'Test Score',message= "You got an D! Try a little harder please!")
    if add_score >=0 and add_score<59.5:
        messagebox.showinfo(title = 'Test Score',message= "You got an F! Work Harder, Try Harder, and STUDY WAY HARDER!!!")


    # TODO) Ask the user for their score on the SECOND test and store their
    #  score in a variable

    # TODO) Take the average score of both tests (total score / 2)

    # TODO) Use if statements to check the average score and print the
    #  corresponding letter grade back to the user. Also, give a different
    #  message according to their grade. Example, for an 'A' grade:
    #  "Wow! You must have studied really hard for those tests!"
    pass
