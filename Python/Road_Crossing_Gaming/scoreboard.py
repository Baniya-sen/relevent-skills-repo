from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        """Creates a scoreboard"""
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-280, 270)
        self.update_score()

    def update_score(self):
        """Updates the level display"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Arial", 11, "normal"))

    def level_up(self):
        """Updates the level"""
        self.level += 1
        self.update_score()

    def game_over(self):
        """Prints game over if collided"""
        self.goto(0, 0)
        self.write("Game-Over", align="center", font=("Arial", 15, "normal"))
