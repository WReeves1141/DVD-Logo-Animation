"""Programmer: Walter Reeves"""
from dvd import Dvd
from counter import Counter
from time import sleep
from turtle import Screen, Turtle


def draw_border() -> None:
    """Draws the screen border."""
    global screen_width, screen_height

    tim = Turtle()
    tim.color("white")
    tim.hideturtle()
    tim.penup()
    tim.goto(screen_width, screen_height)

    tim.pendown()
    for side in range(2):
        tim.right(90)
        tim.forward(screen_height * 2)
        tim.right(90)
        tim.forward(screen_width * 2)
    tim.penup()


def check_corner() -> bool:
    """Checks if the dvd logo hit the corner."""
    global screen_width, screen_height

    if (dvd.xcor() == screen_width - 40 and
            dvd.ycor() == screen_height - 20):
        is_corner = True    # (+, +) Top right corner.
    elif (dvd.xcor() == screen_width * -1 + 40 and
          dvd.ycor() == screen_height - 20):
        is_corner = True    # (-, +) Top left corner.
    elif (dvd.xcor() == screen_width * -1 + 40 and
          dvd.ycor() == screen_height * -1 + 20):
        is_corner = True    # (-, -) Bottom left corner.
    elif (dvd.xcor() == screen_width - 40 and
          dvd.ycor() == screen_height * -1 + 20):
        is_corner = True    # (+, -) Bottom right corner.
    else:
        is_corner = False

    return is_corner


count = 0
counter = Counter()
dvd = Dvd()

# Creates the screen object.
screen_width = 920
screen_height = 490
screen = Screen()
screen.bgcolor("black")
screen.setup(width=screen_width * 2, height=screen_height * 2)
screen.title("Bouncing DVD Logo")
screen.tracer(0)

draw_border()

try:
    is_active = True
    while is_active:
        dvd.move()
        dvd.write_text()
        sleep(0.05)
        screen.update()

        if check_corner():
            count += 1
            counter.increase_counter(counter=count)

        # Changes y-coordinate when the DVD reaches a horizontal border.
        if (dvd.ycor() > screen_height - 60 or
                dvd.ycor() < screen_height * -1):
            dvd.change_y()

        # Changes x-coordinate when the DVD reaches a vertical borders.
        if (dvd.xcor() > screen_width - 60 or
                dvd.xcor() < (screen_width * -1) + 60):
            dvd.change_x()

except KeyboardInterrupt:
    screen.exitonclick()
