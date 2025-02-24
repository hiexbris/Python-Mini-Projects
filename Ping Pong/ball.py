from turtle import Turtle
import random

angle = [80, 90, 100]


class Ball(Turtle):

    def __init__(self, screen):
        self.screen = screen
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.circle(radius=20)
        self.speed(1)

    def game_start(self):
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(1)
        self.screen.update()

    def hit(self):
        current_heading = self.heading()
        if 0 < current_heading < 90 or 180 < current_heading < 270:
            self.setheading(current_heading+random.choice(angle))
        elif 90 < current_heading < 180 or 270 < current_heading < 360:
            self.setheading(current_heading-random.choice(angle))

    def hit_wall(self):
        current_heading = self.heading()
        if 0 < current_heading < 90 or 180 < current_heading < 270:
            self.setheading(current_heading-random.choice(angle))
        elif 90 < current_heading < 180 or 270 < current_heading < 360:
            self.setheading(current_heading+random.choice(angle))
