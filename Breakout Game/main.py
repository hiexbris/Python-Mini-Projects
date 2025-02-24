from turtle import *
import random, time

randomiser = [0, 0, 0, 0, 1]

screen = Screen()
screen.tracer(0)
screen.listen()
screen.screensize(canvwidth=400, canvheight=800)
screen.bgcolor('black')

plate = Turtle(shape='square')
plate.color('red')
plate.shapesize(stretch_len=5, stretch_wid=0.5)
plate.teleport(0, -250)
plate.penup()

ball = Turtle(shape='square')
ball.color('white')
ball.shapesize(0.5)
ball.penup()

pen = Turtle()
pen.hideturtle()
pen.pencolor('white')
pen.teleport(-600, 250)

k = 5
game_on = False

paddle_list = []


def blocks():
    global paddle_list
    paddle_list = []

    for i in range(0, 8):
        for j in range(0, 12):
            paddle = Turtle(shape='square')
            if i == 0 or i == 1:
                paddle.color('yellow')
            elif i == 2 or i == 3:
                paddle.color('green')
            elif i == 4 or i == 5:
                paddle.color('orange')
            elif i == 6 or i == 7:
                paddle.color('red')
            paddle.shapesize(stretch_len=3, stretch_wid=0.8)
            paddle.teleport(-352+64*j, 200+20*i)
            paddle_list.append(paddle)


def block_bounce():
    global ball_dir
    if ball_dir == 0:
        ball_dir = 3
    elif ball_dir == 3:
        if random.choice(randomiser) == 0:
            ball_dir = 0
        else:
            ball_dir = 1
    elif ball_dir == 1:
        ball_dir = 2
    elif ball_dir == 2:
        if random.choice(randomiser) == 0:
            ball_dir = 1
        else:
            ball_dir = 0


def border_bounce():
    global ball_dir
    if ball_dir == 0:
        ball_dir = 1
    elif ball_dir == 1:
        ball_dir = 0
    elif ball_dir == 2:
        ball_dir = 3
    elif ball_dir == 3:
        ball_dir = 2


def move_right():
    if plate.xcor() != 340:
        plate.setheading(0)
        plate.forward(20)


def move_left():
    if plate.xcor() != -340:
        plate.setheading(-180)
        plate.forward(20)


def border_maker():
    border = Turtle()
    border.hideturtle()
    border.width(20)
    border.color('white')
    border.shape('turtle')
    border.teleport(400, 600)
    border.setheading(270)
    border.forward(1200)

    border.teleport(-400, 600)
    border.forward(1200)


def game():
    global game_on
    game_on = True
    main()


def stop():
    plate.forward(0)


border_maker()
screen.update()
screen.onkeypress(fun=move_left, key='a')
screen.onkeyrelease(fun=stop, key='a')
screen.onkeypress(fun=move_right, key='d')
screen.onkeyrelease(fun=stop, key='d')
screen.onkey(fun=game, key='q')


def main():
    global ball_dir, game_on
    for x in paddle_list:
        x.hideturtle()
        del x
    score = 0
    blocks()
    ball_dir = random.randint(0, 3)
    ball.teleport(0, 0)

    while game_on:
        if ball.xcor() <= -385 or ball.xcor() >= 385:
            border_bounce()

        if ball.ycor() <= -240 and (plate.xcor()-55 <= ball.xcor() <= plate.xcor()+55):
            block_bounce()

        if ball.ycor() >= 185:
            for x in paddle_list:
                if x.xcor()-30 <= ball.xcor() <= x.xcor()+30 and x.ycor()-8 <= ball.ycor() <= x.ycor()+8:
                    paddle_list.remove(x)
                    x.hideturtle()
                    del x
                    score += 1
                    pen.clear()
                    pen.write("{:03d}".format(score), align="center", font=("Press Start 2P", 40, "normal"))
                    block_bounce()
                    screen.update()
                    break

        if ball_dir == 0:
            ball.goto(ball.xcor()+k, ball.ycor()+k)
            screen.update()
        elif ball_dir == 1:
            ball.goto(ball.xcor()-k, ball.ycor()+k)
            screen.update()
        elif ball_dir == 2:
            ball.goto(ball.xcor()-k, ball.ycor()-k)
            screen.update()
        elif ball_dir == 3:
            ball.goto(ball.xcor()+k, ball.ycor()-k)
            screen.update()

        if ball.ycor() >= 400:
            block_bounce()

        if ball.ycor() <= -260:
            for x in paddle_list:
                x.hideturtle()
                del x
            game_on = False

        time.sleep(0.0001)


screen.mainloop()
