
import turtle as t
import colorgram
import random

colors_picked = colorgram.extract('image.jpg', 24)


def get_list_rgb(colors):
    rgb = []
    for color in colors:
        c = (color.rgb.r, color.rgb.g, color.rgb.b)
        rgb.append(c)
    return rgb


def print_dot_line(turtle):
    for _ in range(10):
        turtle.dot(20, random.choice(colors_list))
        turtle.forward(50)


colors_list = get_list_rgb(colors_picked)
print(colors_list)
timmy = t.Turtle()
t.colormode(255)
line = -250.0
timmy.up()
timmy.hideturtle()
for _ in range(10):
    timmy.setpos(-250.0, line)
    print_dot_line(timmy)
    line += 50.0


screen = t.Screen()
screen.exitonclick()
