from turtle import *


class Board(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.penup()
        self.shape('square')
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color('white')

    def up(self):
        if self.ycor()+50 < 340:
            self.setheading(90)
            self.forward(40)
            self.screen.update()

    def down(self):
        if self.ycor()-50 > -340:
            self.setheading(270)
            self.forward(40)
            self.screen.update()



