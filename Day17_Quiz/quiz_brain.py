class Quiz_Brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        self.question_number += 1

    def add_one_score(self):
        self.score += 1

    def play_game(self):
        if self.question_number != len(self.question_list) - 1:
            q = self.question_list[self.question_number]
            response = input(f"{self.question_number}: {q.text} (True/False)?\n")
            if response.lower() == q.answer.lower():
                print("You got it right!")
                self.add_one_score()
            else:
                print("That's wrong.")
            print(f"The correct answer was: {q.answer}.")
            print(f"Your current score is: {self.score}/{self.question_number + 1}\n")
            self.next_question()
            self.play_game()
        else:
            print("You've completed the quiz!")
            print(f"Your final score is {self.score}/{self.question_number + 1}")