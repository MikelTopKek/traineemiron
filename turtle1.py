import time
import turtle


def triangle():
    for _ in range(3):
        turtle.forward(20)
        turtle.left(120)


if __name__ == "__main__":
    turtle.shape("turtle")
    turtle.speed(10)
    step = 0
    leng = 20
    col = 20
    triangle()
    # turtle.forward(leng)
    for i in range(1, col):
        turtle.penup()
        turtle.right(180)
        turtle.forward((i + 1) * 0.5 * leng + (i - 1) * step)
        turtle.left(90)
        turtle.forward(leng)
        turtle.left(90)
        for j in range(i + 2):
            turtle.pendown()
            triangle()
            turtle.penup()
            turtle.forward(leng + step)
        turtle.left(180)
        turtle.forward(leng + step)
        turtle.forward((i + 1) * 0.5 * leng + (i - 1) * step)
        turtle.left(180)
    time.sleep(5)
