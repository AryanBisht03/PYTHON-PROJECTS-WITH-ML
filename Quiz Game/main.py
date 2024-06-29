from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank=[]
for questions_and_answers in question_data:
    question=questions_and_answers["text"]
    answer=questions_and_answers["answer"]
    object=Question(question,answer)
    question_bank.append(object)

new_quiz=QuizBrain(question_bank)
while new_quiz.still_has_questions()==True:
    new_quiz.question_answer()

print("The quiz is over")
print(f"You have got {new_quiz.score}/{len(question_bank)}")
