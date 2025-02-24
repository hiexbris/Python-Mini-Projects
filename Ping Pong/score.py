from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super(). __init__()
        self.penup()
        self.pencolor('white')
        self.hideturtle()

    def writer(self, score_left, score_right):
        self.teleport(x=0, y=250)
        self.write(f"{score_left}     {score_right}", align='center', font=('Arial', 60, 'normal'))