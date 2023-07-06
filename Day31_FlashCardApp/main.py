from tkinter import *
import pandas as pd
import random
import json
import os

# =========
# CONSTANTS
# =========
TIMER = 3
INCORRECT_JSON = "incorrect.json"
CORRECT_JSON = "correct.json"
WORD_LIST_JSON = "word_list.json"
GREEN = "#e8f4ea"

# ============
# Window setup
# ============

window = Tk()
window.title("Chinese HSK Character Test")
window.minsize(width=500, height=400)
window.config(padx=40, pady=30, background="#faf0e6")

# ==========
# Data setup
# ==========
# The raw csv needed some work

df = pd.read_csv("New_HSK_2010.csv")
# this is kinda tricky
# the final structure is {row[1}:row[3]}, DO NOT wrap everything in {} notation, just the first part
data = [{"Word": row[1], "Definition": row[3]} for _, row in df.iterrows()]

# Create the word list that keeps tracks of all word that is not guessed yet if it doesn't exist yet
if os.path.isfile(WORD_LIST_JSON):
    print("word_list.json exist")
else:
    with open(WORD_LIST_JSON, mode="w") as file:
        json.dump(data, file, indent=4)

# ============
# Canvas setup
# ============

canvas = Canvas(width=420, height=250)
canvas.config(bg="pink")
word_text = canvas.create_text(220, 75, text="", font=("Arial", 40, "bold"))
def_text = canvas.create_text(220, 150, text="", font=("Arial", 15, "italic"), width=400)
# You have to add the pady here not in the button for some reason???
canvas.grid(column=0, row=0, columnspan=2, pady=10)


# ===========================
# Event Listener and Function
# ===========================
# function to count_down
# function to choose a new word
# function to move card to different folder

def new_word():
    word = random.choice(data)
    canvas.itemconfig(word_text, text=word["Word"])
    return word


def count_down(timer):
    if timer > 0:
        window.after(1000, count_down, timer - 1)
        canvas.config(bg="pink")
    else:
        canvas.itemconfig(def_text, text=current_word["Definition"])
        canvas.config(bg=GREEN)


def write_to_file(fileName):
    global current_word
    try:
        with open(fileName, mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open(fileName, mode="w") as file:
            json.dump(current_word, file, indent=4)
    else:
        data.update(current_word)
        with open(fileName, mode="w") as file:
            json.dump(data, file, indent=4)
    finally:
        canvas.itemconfig(def_text, text="")


def click_x():
    global current_word
    write_to_file(INCORRECT_JSON)
    current_word = new_word()
    count_down(TIMER)


def click_check():
    global current_word
    write_to_file(CORRECT_JSON)
    current_word = new_word()
    count_down(TIMER)


# ==========
# Init setup
# ==========

current_word = new_word()
count_down(TIMER)

# ============
# button setup
# ============

x_image = PhotoImage(file="resized_x_mark.png")
x_button = Button(image=x_image, highlightthickness=0, pady=300, command=click_x)
x_button.grid(column=0, row=1)

check_image = PhotoImage(file="resized_check_mark.png")
check_button = Button(image=check_image, highlightthickness=0, pady=200, command=click_check)
check_button.grid(column=1, row=1)

window.mainloop()
