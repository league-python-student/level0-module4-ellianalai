"""
Use boolean variables to control program logic between two different code
paths.
"""

import turtle
if __name__ == '__main__':


    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    is_weekend=False
    is_not_weekend=True
    if is_weekend:
        print('It is the weekend!! Hooray!!')
    else:
        print('It is not the weekend:(. Go to school now')
    if is_not_weekend:
        print('You sit in school hoping for the weekend to come soon')

    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    pass_exam = False
    did_not_pass_exam = True
    if pass_exam:
        print('You did Great!!')
    else:
        print('You did not take a quiz so you do not get a grade')
    if did_not_pass_exam:
        print('You wish the school day will last forever as you dread when you have to show your mom the quiz')
    game_over=True
    if game_over:
        print('You lost, please try again')
    else:
        print('You do not even know what game to play so you decide to read a book.')

    ellie=turtle.Turtle()
    is_red = True
    is_square = True
    if is_red:
        ellie.pencolor('red')
    if is_square:
        for i in range(2):
            ellie.forward(50)
            ellie.right(90)
            ellie.forward(50)
            ellie.right(90)
    turtle.done()
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    pass
