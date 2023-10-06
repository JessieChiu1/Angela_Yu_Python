from flask import Flask, url_for
import random

# ==========
# init Flask
# ==========

app = Flask(__name__)

# =============
# Pick a number
# =============

chosen_number = random.choice(range(0, 10))
print(chosen_number)


# ================
# Python Decorator
# ================

def generate_number_links():
    number_links = ""
    for number in range(10):
        number_links += f"<button style='margin: 5px; padding: 5px;'>" \
                        f"<a href='{url_for('number_page', number=number)}'>{number}</a>" \
                        f"</button>"
    return number_links


# ===========
# API routing
# ===========


@app.route("/")
def homepage():
    return generate_number_links() + "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"


@app.route("/<number>")
def number_page(number):
    guess = int(number)
    html = ""
    if guess < chosen_number:
        html = "<h1>Too Low<h1>" \
               "<img src=' https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"
    if guess > chosen_number:
        html = "<h1>Too High<h1>" \
               "<img src=' https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>"
    if guess == chosen_number:
        html = "<h1>You guessed correctly<h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>"
    return generate_number_links() + html


# ==============
# Activate Flask
# ==============

if __name__ == "__main__":
    app.run(debug=True)
