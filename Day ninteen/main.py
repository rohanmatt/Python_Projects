from turtle import Turtle, Screen

lol = Turtle()
screen = Screen()


def move_forwards():
    lol.forward(10)

def move_backwards():
    lol.backward(10)

def turn_left():
    new_heading = lol.heading() + 10
    lol.setheading(new_heading)

def turn_right():
    new_heading = lol.heading() - 10
    lol.setheading(new_heading)

def clear():
    lol.clear()
    lol.penup()
    lol.home()
    lol.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
