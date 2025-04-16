import turtle

# Recursive function to draw Koch curve
def koch_curve(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_curve(length, level - 1)
        turtle.left(60)
        koch_curve(length, level - 1)
        turtle.right(120)
        koch_curve(length, level - 1)
        turtle.left(60)
        koch_curve(length, level - 1)

# Setup turtle window
turtle.speed(0)
turtle.bgcolor("black")
turtle.pencolor("cyan")
turtle.penup()
turtle.goto(-150, 90)
turtle.pendown()

# Draw Koch Snowflake (3 Koch curves forming a triangle)
for _ in range(3):
    koch_curve(300, 3)  # 300 is the total length, 3 is the recursion depth
    turtle.right(120)

# Finish
turtle.hideturtle()
turtle.done()

