from quiz_api_setup import *

# ========
# CONSTANT
# ========
QUESTIONS = []

# ============
# Window setup
# ============

window = Tk()
window.title("Quiz")
window.minsize(width=700, height=600)
window.config(padx=50, pady=30)


# ==============
# Quiz API setup
# ==============

quiz_api_parameter_setup(window)

# =============
# Gameplay loop
# =============

while len(QUESTIONS) > 0:
    pass

window.mainloop()
