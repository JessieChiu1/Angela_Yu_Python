import random
from tkinter import *
import requests
import html

# https://docs.python.org/3/library/html.html#html.unescape

# Working with multiple listbox is very messy - need to set exportselection=False to have them work properly
# https://stackoverflow.com/questions/10048609/how-to-keep-selections-highlighted-in-a-tkinter-listbox

# ========
# CONSTANT
# ========
QUESTIONS = []
categories_list = requests.get(url="https://opentdb.com/api_category.php")
CATEGORIES = categories_list.json()["trivia_categories"]

CATEGORY = None
NUM_QUESTIONS = 1
DIFFICULTY = None
TYPE = None
score = 0
widgets = []

# ============
# Window setup
# ============

window = Tk()
window.title("Quiz")
window.minsize(width=700, height=600)
window.config(padx=50, pady=30)


def clear_widgets():
    for widget in widgets:
        widget.destroy()


canvas = Canvas(width=600, height=400)
question_text = canvas.create_text(300, 200, text="", font=("Arial", 20, "bold"))
canvas.grid(column=0, row=0, columnspan=4, pady=10)

# ==============
# Quiz API setup
# ==============

# Selecting Category
# ==================
def select_category(event):
    global CATEGORY
    selected_category = categories_listbox.get(categories_listbox.curselection())
    if selected_category == "Any Category":
        CATEGORY = None
    for category in CATEGORIES:
        if category["name"] == selected_category:
            CATEGORY = category["id"]


categories_listbox = Listbox(height=len(CATEGORIES), exportselection=False, width=40)
categories_listbox.insert(0, "Any Category")
for category in CATEGORIES:
    categories_listbox.insert(END, category["name"])

categories_listbox.bind("<<ListboxSelect>>", select_category)
categories_listbox.grid(column=0, row=0, padx=5, pady=5)
widgets.append(categories_listbox)


# Selecting number of questions
# =============================
def spinbox_used():
    global NUM_QUESTIONS
    NUM_QUESTIONS = spinbox.get()


spinbox = Spinbox(from_=1, to=50, width=5, command=spinbox_used)
spinbox.grid(column=1, row=0, padx=5, pady=5)
widgets.append(spinbox)

# Selecting Difficulty
# ====================

difficulties = ["Any Difficulty", "easy", "medium", "hard"]


def select_difficulty(event):
    global DIFFICULTY
    selected_diff = diff_listbox.get(diff_listbox.curselection())
    if selected_diff == "Any Difficulty":
        DIFFICULTY = None
    else:
        DIFFICULTY = selected_diff


diff_listbox = Listbox(height=len(difficulties), exportselection=False)
for diff in difficulties:
    diff_listbox.insert(END, diff)

diff_listbox.bind("<<ListboxSelect>>", select_difficulty)
diff_listbox.grid(column=2, row=0, padx=5, pady=5)
widgets.append(diff_listbox)

# Selecting Type
# ==============
types = ["Any", "Multiple Choice", "True/False"]


def select_type(event):
    global TYPE
    selected_type = type_listbox.get(type_listbox.curselection())
    if selected_type == "Any":
        TYPE = None
    elif selected_type == "Multiple Choice":
        TYPE = "multiple"
    elif selected_type == "True/False":
        TYPE = "boolean"


type_listbox = Listbox(height=len(types), exportselection=False)
for t in types:
    type_listbox.insert(END, t)

type_listbox.bind("<<ListboxSelect>>", select_type)
type_listbox.grid(column=3, row=0, padx=5, pady=5)
widgets.append(type_listbox)


# Fetching API
# ============

def fetching_questions():
    global QUESTIONS
    url = "https://opentdb.com/api.php" + f"?amount={NUM_QUESTIONS}"
    if CATEGORY is not None:
        url += f"&category={CATEGORY}"
    if DIFFICULTY is not None:
        url += f"&difficulty={DIFFICULTY}"
    if TYPE is not None:
        url += f"&type={TYPE}"
    response = requests.get(url)
    QUESTIONS = response.json()["results"]


# Once the button in the quiz API setup is click
# we will fetch the questions based on user's prompt
# clear all the quiz API widget
# start the quiz
def button_click():
    global QUESTIONS
    fetching_questions()
    clear_widgets()
    canvas.config(bg="pink")
    # start the quiz gameplay loop
    start_quiz()


button = Button(text="Start Quiz", command=button_click)
button.grid(column=4, row=0, padx=5, pady=5)
widgets.append(button)


# =============
# Gameplay loop
# =============
def start_quiz():
    global QUESTIONS
    global score
    if QUESTIONS:
        gameplay_loop()


# each gamplay loop render the question's text and create a button for each possible answers
def gameplay_loop():
    # choose and set question's text on canvas
    current_question = random.choice(QUESTIONS)
    # must use html.unescape(TEXT) to translate the text to more readable text
    canvas.itemconfig(question_text, text=html.unescape(current_question["question"]), width=580)
    # append all possible answers into a list and shuffle it
    answers = current_question["incorrect_answers"]
    answers.append(current_question["correct_answer"])
    random.shuffle(answers)

    # create a button for each answer
    for answer in answers:
        # must use html.unescape(TEXT) to translate the text to more readable text
        answer_button = Button(text=html.unescape(answer), width=20, wraplength=100, padx=5,
                               command=lambda event, q=current_question: click_answer(event, q))
        answer_button.grid(column=answers.index(answer), row=1, padx=5, pady=5)
        answer_button.bind("<Button-1>", lambda event, q=current_question: click_answer(event, q))
        widgets.append(answer_button)


# function that is fire after an answer is clicked
def click_answer(event, question):
    global score
    # cast the button being click to a variable and grab the text
    answer_button = event.widget
    answer = answer_button.cget("text")
    # compare answer to the html.unescape(correct_answer)
    if answer == html.unescape(question["correct_answer"]):
        score += 1
    # remove the question from the QUESTIONS list
    QUESTIONS.remove(question)
    # remove all the button
    clear_widgets()
    # run the gameplay loop again if there is still questions left
    if QUESTIONS:
        gameplay_loop()
    # print score
    else:
        canvas.itemconfig(question_text, text=f"Quiz Completed, Your final score is {score}/{NUM_QUESTIONS}")


window.mainloop()
