class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        if user_answer == question.answer:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was : {question.answer}")
            print(f"Your current score is: {self.score}/{self.question_number}.")
            print("\n")
        else:
            print("You got it wrong")
            print(f"The correct answer was: {question.answer}")
            print(f"Your current score is: {self.score}/{self.question_number}.")
            print("\n")