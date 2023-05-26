from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

question_bank = []

for q in question_data:

    new_q = Question(q["text"],q["answer"])
    question_bank.append(new_q)

quiz_brain = Quiz_Brain(question_bank)

quiz_brain.play_game()