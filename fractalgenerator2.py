import turtle
import random

# Set up turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw a filled triangle with color
def draw_triangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.begin_fill()
    for point in points[1:] + [points[0]]:
        t.goto(point)
    t.end_fill()

# Get the midpoint between two points
def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Recursive function to draw Sierpinski triangle
def sierpinski(points, level):
    colors = ['cyan', 'magenta', 'yellow', 'lime', 'orange', 'deep pink', 'aqua']
    draw_triangle(points, random.choice(colors))
    if level > 0:
        sierpinski([points[0],
                    midpoint(points[0], points[1]),
                    midpoint(points[0], points[2])], level - 1)
        sierpinski([points[1],
                    midpoint(points[0], points[1]),
                    midpoint(points[1], points[2])], level - 1)
        sierpinski([points[2],
                    midpoint(points[2], points[1]),
                    midpoint(points[0], points[2])], level - 1)

# Initial triangle points
initial_points = [(-200, -100), (0, 200), (200, -100)]
sierpinski(initial_points, 5)  # You can increase the level for more detail

turtle.done()
