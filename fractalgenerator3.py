# sierpinski.py
import turtle
import random

def draw_triangle(t, points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.begin_fill()
    for pt in points[1:] + [points[0]]:
        t.goto(pt)
    t.end_fill()

def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(t, points, level):
    palette = ['#00FFFF', '#FF00FF', '#FFFF00', '#00FF00', '#FFA500', '#FF1493', '#7FFFD4']
    draw_triangle(t, points, random.choice(palette))
    if level > 0:
        sierpinski(t, [points[0],
                       midpoint(points[0], points[1]),
                       midpoint(points[0], points[2])], level - 1)
        sierpinski(t, [points[1],
                       midpoint(points[0], points[1]),
                       midpoint(points[1], points[2])], level - 1)
        sierpinski(t, [points[2],
                       midpoint(points[2], points[1]),
                       midpoint(points[0], points[2])], level - 1)

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    size = 300
    points = [(-size, -size / 2), (0, size), (size, -size / 2)]
    sierpinski(t, points, 5)

    turtle.done()

if __name__ == "__main__":
    main()
