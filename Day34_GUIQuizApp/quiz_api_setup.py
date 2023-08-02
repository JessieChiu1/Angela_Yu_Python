import random
from tkinter import *
import requests

# Working with multiple listbox is very messy - need to set exportselection=False to have them work properly
# https://stackoverflow.com/questions/10048609/how-to-keep-selections-highlighted-in-a-tkinter-listbox

# ========
# CONSTANT
# ========

categories_list = requests.get(url="https://opentdb.com/api_category.php")
CATEGORIES = categories_list.json()["trivia_categories"]

CATEGORY = None
NUM_QUESTIONS = 1
DIFFICULTY = None
TYPE = None


# ==================
# Quiz Widgets setup
# ==================

def quiz_canvas_setup():
    canvas = Canvas(width=600, height=400)
    canvas.config(bg="pink")
    question_text = canvas.create_text(300, 200, text="", font=("Arial", 20, "bold"))
    canvas.grid(column=0, row=0, columnspan=4)

# =============
# Gameplay Loop
# =============

def render_question(QUESTIONS):
    question = random.choice(QUESTIONS)
    choices = question["correct"]


# ==============
# Quiz API setup
# ==============

def quiz_api_parameter_setup(window):
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

    categories_listbox = Listbox(height=len(CATEGORIES), exportselection=False)
    categories_listbox.insert(0, "Any Category")
    for category in CATEGORIES:
        categories_listbox.insert(END, category["name"])

    categories_listbox.bind("<<ListboxSelect>>", select_category)
    categories_listbox.grid(column=0, row=0)

    # Selecting number of questions
    # =============================
    def spinbox_used():
        global NUM_QUESTIONS
        NUM_QUESTIONS = spinbox.get()

    spinbox = Spinbox(from_=1, to=50, width=5, command=spinbox_used)
    spinbox.grid(column=1, row=0)

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
    diff_listbox.grid(column=2, row=0)

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
    type_listbox.grid(column=3, row=0)

    # Fetching API
    # ============

    def const_url():
        url = "https://opentdb.com/api.php" + f"?amount={NUM_QUESTIONS}"
        if CATEGORY is not None:
            url += f"&category={CATEGORY}"
        if DIFFICULTY is not None:
            url += f"&difficulty={DIFFICULTY}"
        if TYPE is not None:
            url += f"&type={TYPE}"
        return url

    def clear_widgets():
        for widget in window.winfo_children():
            widget.destroy()

    def button_click():
        # get questions
        url = const_url()
        response = requests.get(url=url)
        QUESTIONS = response.json()["results"]
        # clear all the widgets
        clear_widgets()
        # setup question canvas
        quiz_canvas_setup()

    button = Button(text="Start Quiz", command=button_click)
    button.grid(column=4, row=0)
