from turtle import Turtle, Screen
import random
import time


screen = Screen()
screen.screensize(500, 400)
screen.bgcolor("black")
snake_list = []
screen.tracer(0)

score_teller = Turtle()
score_teller.hideturtle()
score_teller.pencolor("white")
score_teller.penup()
score_teller.setpos(0, 275)
score_teller.write("Score: 0", align="center", font=("Arial", 16, "normal"))

food = Turtle(shape="circle")
food.teleport(x=random.randint(-340, 340), y=random.randint(-290, 250))
food.color("blue")
food.shapesize(0.25)
food.penup()

for i in range(3):
    snake = Turtle("square")
    snake.color("red")
    snake.speed(1)
    snake.penup()
    snake_list.append(snake)

t = 3


def snake_maker(i):
    new_tail = Turtle("square")
    new_tail.hideturtle()
    x_new = snake_list[i-1].xcor()
    y_new = snake_list[i-1].ycor()
    heading_1 = snake_list[i-1].heading()
    new_tail.color('red')
    new_tail.speed(1)
    new_tail.penup()
    if heading_1 == 0:
        new_tail.teleport(x=x_new-10, y=y_new)
    elif heading_1 == 180:
        new_tail.teleport(x=x_new+10, y=y_new)
    elif heading_1 == 90:
        new_tail.teleport(x=x_new, y=y_new-10)
    elif heading_1 == 270:
        new_tail.teleport(x=x_new, y=y_new+10)
    new_tail.showturtle()
    snake_list.append(new_tail)


screen.listen()
game_on = True


def food_spawn(score):
    global t
    score -= 2
    food.teleport(x=random.randint(-340, 340), y=random.randint(-290,250))
    snake_maker(t)
    t += 1
    score_teller.clear()
    score_teller.write(f"Score: {score*100}", align='center', font=("Arial", 16, "normal"))
    if score % 3 == 0:
        speed = snake_list[0].speed()
        snake_list[0].speed(speed+1)


def up():
    if snake_list[0].heading() != 270:
        speed = snake_list[0].speed()
        snake_list[0].speed(0)
        snake_list[0].setheading(90)
        snake_list[0].speed(speed)


def down():
    if snake_list[0].heading() != 90:
        speed = snake_list[0].speed()
        snake_list[0].speed(0)
        snake_list[0].setheading(270)
        snake_list[0].speed(speed)


def right():
    if snake_list[0].heading() != 180:
        speed = snake_list[0].speed()
        snake_list[0].speed(0)
        snake_list[0].setheading(0)
        snake_list[0].speed(speed)


def left():
    if snake_list[0].heading() != 0:
        speed = snake_list[0].speed()
        snake_list[0].speed(0)
        snake_list[0].setheading(180)
        snake_list[0].speed(speed)


screen.onkey(key="Left", fun=left)
screen.onkey(key="Up", fun=up)
screen.onkey(key="Right", fun=right)
screen.onkey(key="Down", fun=down)

snake_list[0].speed(1)
score = len(snake_list)
while game_on:
    for i in range(1, score):
        if i == score-1:
            x_new = snake_list[0].xcor()
            y_new = snake_list[0].ycor()
        else:
            x_new = snake_list[-i-1].xcor()
            y_new = snake_list[-i-1].ycor()
        snake_list[-i].teleport(x=x_new, y=y_new)
    snake_list[0].forward(20)
    screen.update()
    time.sleep(0.1)
    x_head = snake_list[0].xcor()
    y_head = snake_list[0].ycor()
    food_x = food.xcor()
    food_y = food.ycor()
    if abs(x_head-food_x) < 10 and abs(y_head-food_y) < 10:
        score += 1
        food_spawn(score-1)
    for i in snake_list[1:]:
        x_body = i.xcor()
        y_body = i.ycor()
        if abs(x_head-x_body) < 10 and abs(y_head-y_body) < 10:
            game_on = False
    if x_head > 350 or x_head < -360 or y_head > 300 or y_head < -300:
        game_on = False

over = Turtle()
over.hideturtle()
over.pencolor("white")
over.penup()
over.write("GAME OVER", align="center", font=("Arial", 30, "normal"))

screen.exitonclick()