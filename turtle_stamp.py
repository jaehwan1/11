import turtle
import random

def screenLeftClick(x, y):
    tSize = random.randrange(2, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color((r, g, b))
    tAngle = random.randrange(0, 360)

    turtle.penup()
    turtle.goto(x, y)
    turtle.left(tAngle)
    turtle.stamp()

tSize, tAngle = 0, 0
r, g, b = 0.0, 0.0, 0.0

turtle.title('거북이 도장 찍는 프로그램')
turtle.shape('turtle')

turtle.onscreenclick(screenLeftClick, 1)

turtle.done()