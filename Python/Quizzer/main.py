from question_model import Questions
from data import question_data
from quiz_brain import QuizzBrain
from ui import QuizInterface

# Creates a list of Questions class instance
question_bank = []

# Looping through raw questions data and passing to Questions class
for question in question_data:
    question_bank.append(Questions(
        text=question["question"],
        answer=question["correct_answer"])
    )

# Instances / Main loop
quizz = QuizzBrain(questions_list=question_bank)
ui = QuizInterface(quizz)
