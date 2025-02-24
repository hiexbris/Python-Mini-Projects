from turtle import Turtle, Screen
import random
screen = Screen()
screen.screensize(500, 400)
bet = screen.textinput(title="place your bet", prompt="which turtle will win")
colors = ["red", 'yellow', 'purple', 'green', 'blue']
turtle_list = []
y_coords = [-80, -40, 0, 40, 80]
game_on = False

finish_line = Turtle()
finish_line.penup()
finish_line.goto(x=230, y=-100)
finish_line.pendown()
finish_line.pencolor('red')
finish_line.goto(x=230, y=100)

for i in range(0, 5):
    list_1 = Turtle(shape="turtle")
    list_1.color(colors[i])
    list_1.penup()
    list_1.goto(x=-230, y=y_coords[i])
    turtle_list.append(list_1)

game_on = True

while game_on:
    for i in turtle_list:
        i.forward(random.randint(0, 10))
        if i.xcor() >= 230:
            game_on = False
            winner = i.pencolor()

if bet == winner:
    print(f"You won, {winner} won the race")
else:
    print(f"You lost, {winner} won the race")
screen.exitonclick()