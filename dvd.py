"""Programmer: Walter Reeves"""
from turtle import Turtle
import random

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Magenta"]
current_color = ""


class Dvd(Turtle):
    """Represents each DVD logo."""

    def __init__(self, x_move_amount=11, y_move_amount=11):
        super().__init__()
        global colors, current_color

        current_color = random.choice(colors)
        self.color(current_color)
        self.penup()
        self.write_text()
        self.hideturtle()
        self.x_move = x_move_amount
        self.y_move = y_move_amount

    def move(self) -> None:
        """Moves DVD until it hits the border."""
        self.clear()
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)
        self.write_text()

    def change_x(self) -> None:
        """Changes x-coordinate direction."""
        global current_color

        self.x_move *= -1
        self.new_color(current_color)

    def change_y(self) -> None:
        """Changes y-coordinate direction."""
        self.y_move *= -1
        self.new_color(current_color)

    def write_text(self) -> None:
        """Displays DVD logo to the screen."""
        self.write("DVD", align="center", font=("Comic Sans", 48, "bold"))

    def new_color(self, current) -> None:
        """Changes the current DVD logo color."""
        global current_color

        new = random.choice(colors)
        while new == current:
            new = random.choice(colors)

        current_color = new
        self.color(new)
