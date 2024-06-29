class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score=0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def question_answer(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        current_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False)?:")
        self.check_answer(current_answer, current_question.answer)

    def check_answer(self, current_answer, correct_answer):
        if current_answer.lower() == correct_answer.lower():
            self.score+=1
            print("Your answer is correct")
        else:
            print("Your answer is incorrect")
        print(f'The correct answer is {correct_answer}')
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

