from turtle import Turtle

# Constants
ALIGNMENT = "CENTER"
FONT = ("16 point Consolas", 11, "bold")


class Score(Turtle):
    """Creates a score-card at top of the window"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 275)
        self.score = 0
        self.update_score()

    def update_score(self):
        """Updates score everytime user hits a food"""
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        """Print game-over when user hits a wall or collide snake with its own tail"""
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)
