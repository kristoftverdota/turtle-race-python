from turtle import Turtle, Screen
import random

race_on = False

screen = Screen()
screen.setup(width=1000, height=800)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
print(user_bet)

color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-200, -100, 0, 100, 200, 300]
turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-470, y=y_pos[i])
    turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 480:
            winner = turtle.pencolor()
            race_on = False
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
