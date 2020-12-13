import turtle
import time


def triangle():
    for _ in range(3):
        turtle.forward(20)
        turtle.left(120)
    turtle.forward(20)


if __name__ == "__main__":
    turtle.shape("turtle")

    triangle()
    for i in range(1, 4):
        turtle.penup()
        turtle.right(180)
        turtle.forward(25*(i+1))
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        for j in range(i+2):
            turtle.pendown()
            triangle()
            turtle.penup()
            turtle.forward(10)
        turtle.left(180)
        turtle.forward(25*(i+1))
        turtle.left(180)

    time.sleep(5)


