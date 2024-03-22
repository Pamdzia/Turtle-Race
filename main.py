from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour "
                                                          "red, orange, yellow, green, blue, purple: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(6):
    tutel = Turtle(shape="turtle")
    tutel.color(colors[turtle_index])
    tutel.penup()
    tutel.goto(-230, y_positions[turtle_index])
    all_turtles.append(tutel)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You win. The {winning_colour} turtle is the winner!")
            else:
                print(f"You lose. The {winning_colour} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
