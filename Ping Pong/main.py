import turtle
import score
import board
import ball
import time

screen = turtle.Screen()
screen.setup(width=1200, height=700)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)
score_show = score.Score()
score_left = 0
score_right = 0
ball = ball.Ball(screen)
board_left = board.Board(screen)
board_left.teleport(x=-585, y=0)
board_right = board.Board(screen)
board_right.teleport(x=580, y=0)
screen.update()
screen.onkey(fun=board_left.up, key='w')
screen.onkey(fun=board_left.down, key='s')
screen.onkey(fun=board_right.up, key='Up')
screen.onkey(fun=board_right.down, key='Down')
lines = turtle.Turtle()
lines.color('white')
lines.teleport(x=0, y=-340)
lines.setheading(90)
lines.hideturtle()


def write():
    lines.forward(60)
    lines.penup()
    lines.forward(30)
    lines.pendown()


for _ in range(8):
    write()

while True:
    game_on = True
    score_show.clear()
    score_show.writer(score_left, score_right)
    ball.goto(x=0, y=0)
    ball.game_start()
    screen.update()
    time.sleep(0.5)
    while game_on:
        ball.move()
        time.sleep(0.0001)
        xcor = ball.xcor()
        ycor = ball.ycor()
        if -566 <= xcor <= -564:
            ycor_left = board_left.ycor()
            if ycor_left-50 <= ycor <= ycor_left+50:
                ball.hit()
                ball.forward(3)
                screen.update()
        elif 559 <= xcor <= 561:
            ycor_right = board_right.ycor()
            if ycor_right-50 <= ycor <= ycor_right+50:
                ball.hit()
                ball.forward(3)
                screen.update()
        elif xcor >= 590 or xcor <= -595:
            game_on = False
        elif 339 <= ycor <= 341 or -341 <= ycor <= -339:
            ball.hit_wall()
            ball.forward(3)
            screen.update()

    if ball.xcor() > 0:
        score_left += 1
    elif ball.xcor() < 0:
        score_right += 1




