from turtle import Turtle
from player import Player

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle, Player):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.prompt()

    def prompt(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.write(f'Level:{self.score}', align='left', font = FONT)

    def keep_score(self):
        if Player.refresh() == True:
            self.score += 1
