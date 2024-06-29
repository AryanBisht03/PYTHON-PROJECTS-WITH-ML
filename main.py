# # class User:
# #     pass
# #
# #     def user():
# #         pass
# #
# #
# # user1 = User()
# # user1.id="001"
# # user1.username="Aryan"
# # user1.age=23
# # user1.studentid=20011326
# # user1.Urollnumber=2018226
# # print(user1.id)
# # print(user1.username)
# # print(user1.age)
# # print(user1.studentid)
# # print(user1.Urollnumber)
# #
#
# class User:
#     def __init__(self,username,id,age):
#         self.username=username
#         self.id=id
#         self.age=age
#         self.followers=0
#         self.gate_score=0
#     def info(self):
#         print(f"The user name is {self.username}")
#         print(f"The user id is {self.id}")
#         print(f"The user age is {self.age}")
#         print(f"The user followers are {self.followers}")
#         print(f"The user gate score is {self.gate_score}")
#
#
# user1=User("Aryan",100,23)
# user1.followers=23
# user1.gate_score=45
# user1.info()

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