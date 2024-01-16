from tkinter import *
from quiz_brain import QuizzBrain


class QuizInterface:
    def __init__(self, quiz: QuizzBrain):
        """Creates a UI for Quizzer"""
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg="#375362")

        self.score_label = Label(text="Score: 1", bg="#375362", fg="white", font=("Ariel", 12, "bold"))
        self.score_label.grid(column=1, row=0, columnspan=2)

        self.canvas = Canvas(width=400, height=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            200,
            150,
            width= 380,
            text="Question-",
            font=("Ariel", 15, "normal"))
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false_press)
        self.wrong_button.config(pady=20)
        self.wrong_button.grid(column=1, row=4)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.true_press)
        self.right_button.config(pady=20)
        self.right_button.grid(column=2, row=4)

        # Get a question to display
        self.next_question()

        # Main window loop
        self.window.mainloop()

    def next_question(self):
        """Prints the question to UI"""
        # Reset canvas color, and enables both buttons
        self.canvas.config(bg="white")
        self.wrong_button.config(state="normal")
        self.right_button.config(state="normal")

        # If question are left, Update score, and display question
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You have completed the quizz.")
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def false_press(self):
        """Detects a False button press"""
        self.wrong_button.config(state="disabled")
        self.right_button.config(state="disabled")
        self.feedback(self.quiz.check_answer("false"))

    def true_press(self):
        """Detects a True button press"""
        self.wrong_button.config(state="disabled")
        self.right_button.config(state="disabled")
        self.feedback(self.quiz.check_answer("true"))

    def feedback(self, answer):
        """Checks if answer is correct or not"""
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1100, self.next_question)

