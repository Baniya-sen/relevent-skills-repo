class QuizzBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {current_question.text} [True/False]: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("Yeah! You got it right.")
        else:
            print("No! You got it wrong.")

        print(f"Your current score is {self.score}/{self.question_number}", end='\n\n')
