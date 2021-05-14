"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a String variable.
    #  3.1415926535897932384
    pi = '3.1415926535897932384'
    print(pi[0])
    print(pi[2])
    print(pi[3])

    digit = simpledialog.askstring(title ='', prompt= 'What is the next digit of pi?')
    math = 4
    while math < 20:

        if digit == pi[math]:
            messagebox.showinfo(title ='', message = 'You are Correct!')
        else:
            print(math - 4)
            messagebox.showinfo(title='', message='You are incorrect:(')
            break
        math += 1
        digit = simpledialog.askstring(title='', prompt='What is the next digit of pi?')
    if math>=20:
        messagebox.showinfo(title ='',message='You got all twenty correct!')
    else:
        messagebox.showinfo(title='', message='You did not manage to get all twenty correct')
    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit


    # TODO) Use a while loop to keep asking for the next digit of pi

        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
