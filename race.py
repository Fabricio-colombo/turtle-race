from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

def create_turtle(color, x, y):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    return turtle

turtles = []
colors = ['red', 'green', 'blue', 'purple', 'orange', 'yellow', 'pink', 'brown']
start_y_positions = [-70, -50, -30, -10, 10, 30, 50, 70]

for color, y in zip(colors, start_y_positions):
    turtles.append(create_turtle(color, -240, y))

race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations! The {winning_color} turtle won!")
            else:
                print(f"Sorry, the {winning_color} turtle won. Better luck next time!")
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
