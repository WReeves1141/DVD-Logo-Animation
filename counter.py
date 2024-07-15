"""Programmer: Walter Reeves"""
from turtle import Turtle


class Counter(Turtle):
    """Represents the on-screen corner counter."""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, -100)
        self.write("Times hit corner: 0", align="center")

    def increase_counter(self, counter) -> None:
        """Increases the corner hits counter."""
        self.clear()
        self.write(f"Times hit corner: {counter}", align="center")
