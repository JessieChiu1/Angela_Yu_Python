from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain
import requests
import json

res = requests.get("https://opentdb.com/api.php?amount=50&category=15&type=boolean")
data = json.loads(res.text)["results"]

questions_bank = []

for q in data:
    q_fixed = q["question"].replace("&quot;", "\"")
    new_q = Question(q_fixed, q["correct_answer"])
    questions_bank.append(new_q)

quiz_brain = Quiz_Brain(questions_bank)

quiz_brain.play_game()