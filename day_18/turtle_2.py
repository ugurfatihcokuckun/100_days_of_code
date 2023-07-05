# from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()

"""
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red", "green")


# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# screen = Screen()
# screen.exitonclick()
"""


"""
# for _ in range(0,15):
    
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
"""


"""
colours = ["dark turquoise", "blue", "red", "dark goldenrod", "magenta", "dark orchid", "crimson", "dark slate blue"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        
for shape_sides_n in range(3,11):
    tim.color(r.choice(colours))
    draw_shape(shape_sides_n)
"""

"""
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return  random_color


# colours = ["dark turquoise", "blue", "red", "dark goldenrod", "magenta", "dark orchid", "crimson", "dark slate blue"]
direction = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

for _ in range(200):
    # tim.color(random.choice(colours))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))
"""


"""
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
"""

"""
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
color_list = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]

tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
"""