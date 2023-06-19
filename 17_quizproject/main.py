# class User:
#     pass => write pass in functions or class to avoid indent error
# a way to initialize object atrributes
# user_1 = User()
# user_1.id = "001"
# user_1.username = "jaltadeepak" 


# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
# user_1 = User("001", "jaltadeepak")
# user_2 = User("002", "kaafideepak")
# print(user_1.followers)
# user_1.follow(user_2)
# print(user_1.followers, user_1.following)
# print(user_2.followers, user_2.following)

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()