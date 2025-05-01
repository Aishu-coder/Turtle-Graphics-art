from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput(title='Take a guess', prompt='which turtle would win? enter color.')
screen.listen()
race = True
all_turtles = []
colors = ['green', 'red', 'blue', 'yellow', 'purple', ]
y = 100
for turtle_index in range(5):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-220, y=y)
    y -= 50
    all_turtles.append(new_turtle)
while race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race = False
            win = turtle.pencolor()
            if win == guess:
                print(f"You win!the winner is {win}")
            else:
                print(f"You loose!the winner is {win}")
        speed = random.randint(0, 10)
        turtle.forward(speed)
screen.exitonclick()
