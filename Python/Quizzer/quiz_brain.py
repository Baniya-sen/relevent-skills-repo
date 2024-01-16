import html


class QuizzBrain:
    def __init__(self, questions_list):
        """Manage questions to display and tracks user score"""
        self.current_question = None
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        """Checks i questions are left to display"""
        return self.question_number < len(self.questions_list)

    def next_question(self):
        """Gets the next question from list"""
        self.current_question = self.questions_list[self.question_number]
        self.question_number += 1

        # Unescape any hex code
        question = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {question}"

    def check_answer(self, user_input):
        """Checks if user answer is correct or not, and updates score"""
        if user_input == self.current_question.answer.lower():
            self.score += 1
            return True
        else:
            return False
