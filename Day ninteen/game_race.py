from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
race_turtles = []


for turtle_index in range(0, 6):
    lol = Turtle(shape="turtle")
    lol.penup()
    lol.color(colors[turtle_index])
    lol.goto(x=-230, y=y_positions[turtle_index])
    race_turtles.append(lol)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in race_turtles:
        
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()