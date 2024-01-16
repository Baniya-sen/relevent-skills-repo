from question_model import Questions
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []

for question in question_data:
    question_bank.append(Questions(text=question["text"], answer=question["answer"]))

quizz = QuizzBrain(questions_list=question_bank)

while quizz.still_has_questions():
    quizz.next_question()

print("You have completed the quizz.")
print(f"And Your final score is {quizz.score}/{quizz.question_number}.")
