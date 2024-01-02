from turtle import Turtle


class Score(Turtle):
    """Creates a score board for both player"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        """Updates scoreboard every time a player misses"""
        self.clear()
        self.setposition(-60, 255)
        self.write(f"Left score: {self.left_score}", align="center", font=("Arial", 12, "normal"))
        self.setposition(60, 255)
        self.write(f"Right score: {self.right_score}", align="center", font=("Arial", 12, "normal"))

    def left_point(self):
        """Updates score of left player"""
        self.left_score += 1
        self.update_score()

    def right_point(self):
        """Updates score of right player"""
        self.right_score += 1
        self.update_score()
