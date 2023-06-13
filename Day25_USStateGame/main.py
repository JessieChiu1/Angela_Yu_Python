import turtle
from states import State
import pandas as pd

# =========================
# Screen and variable setup
# =========================
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# Disable initial animation
screen.tracer(0)
game_on = True


# ============
# States setup
# ============

dataset = pd.read_csv("50_states.csv").to_dict(orient="records")
# print(dataset)
states_class_list = []

for row in dataset:
    state = State(row["state"], row["x"], row["y"])
    states_class_list.append(state)

# =============
# Gameplay loop
# =============

while game_on:
    # Check win
    if len(states_class_list) == 0:
        print("You guessed them all!")
        game_on = False

    # Gameplay loop
    guess = screen.textinput("Player Input", "Name a State").lower()
    if guess is not None:
        for state in states_class_list:
            if guess == state.name.lower():
                state.reveal_state()
                states_class_list.remove(state)

turtle.mainloop()