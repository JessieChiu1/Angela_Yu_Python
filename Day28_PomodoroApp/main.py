from tkinter import *
import time

# =========
# CONSTANTS
# =========
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#ffffff"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check = '✔️'

# ============
# Window Setup
# ============
window = Tk()
window.minsize(height=400, width=400)
window.config(background=YELLOW, padx=100, pady=100)
window.title("Pomodoro Timer")

# ============
# Canvas setup
# ============
# canvas widget is to put image on top of something
# init the canvas as a place to lay a shape/image on top of something
canvas = Canvas(width=200, height=224)
canvas.config(background=YELLOW, highlightthickness=0)
# open up the image and store it in a variable
photo = PhotoImage(file="tomato.png")
# specify that the canvas will take the shape of the photo variable
canvas.create_image(100, 112, image=photo)
# now we will create the timer text that will lay on top of the image
# cast it to a variable since we will need to retrieve it for the count down function
timer_text = canvas.create_text(100, 130, text="", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# ===================
# Countdown mechanism
# ===================
# setup list of the pomodoro cycle
# button_clicked:
# when the button is click, set the countdown timer in seconds based on the current cycle
# run the count_down function recursively which count down the timer by 1 every second
# and set the formatted time text to the canvas text
# when countdown goes to 0 move on to the next cycle
# if there is no next cycle, just print Done! on where the timer supposed to be


# Pomodoro timer cycle setup
pomodoro_cycle = []
for _ in range(0, 4):
    pomodoro_cycle.append(WORK_MIN)
    pomodoro_cycle.append(SHORT_BREAK_MIN)
pomodoro_cycle.append(LONG_BREAK_MIN)

# convert the integer to time in sec
pomodoro_cycle = [time * 60 for time in pomodoro_cycle]

# Global variable to keep track of the current cycle
current_cycle_index = 0
# Global variable to keep track of the after function running so we can cancel it later
current_timer_id = None


# format time
def format_time(seconds):
    '''
    :param seconds: integer
    :return: time in the format of min:sec
    '''
    minutes, seconds = divmod(seconds, 60)
    return '{:02d}:{:02d}'.format(minutes, seconds)


# countdown - recursion

def count_down(timer, ):
    global current_cycle_index
    global current_timer_id
    if timer > 0:
        current_timer_id = window.after(10, count_down, timer - 1)
        canvas.itemconfig(timer_text, text=format_time(timer))
    # The else statement is when we roll over to the next cycle
    else:
        # move to the next pomodoro cycle and run the function after 1 sec also
        current_cycle_index += 1
        # check if we are at the end of the cycle
        if current_cycle_index == 8:
            canvas.itemconfig(timer_text, text="Done!")
            return
        # NOTE TO JESSIE, for some reason if current_cycle_index == 0 or 2 or 4 or 6 DOES NOT WORK
        if current_cycle_index in [0, 2, 4, 6]:
            sequence_label.config(text="Work")
        else:
            sequence_label.config(text="Break")
        timer = pomodoro_cycle[current_cycle_index]
        current_timer_id = window.after(10, count_down, timer - 1)
        canvas.itemconfig(timer_text, text=format_time(timer))
        # add a check mark
        checkmark = check_label.cget("text")
        checkmark += check
        check_label.config(text=checkmark)


# button event listener when the start button is clicked
def start_clicked():
    sequence_label.config(text="Work")
    current_timer = pomodoro_cycle[current_cycle_index]
    count_down(current_timer)


# ============
# Reset button
# ============

def reset_clicked():
    global current_timer_id
    canvas.itemconfig(timer_text, text='')
    sequence_label.config(text="Timer")
    check_label.config(text='')
    if current_timer_id is not None:
        window.after_cancel(current_timer_id)
        current_timer_id = None


# ============
# Widget setup
# ============

sequence_label = Label(text="Timer", background=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
sequence_label.grid(column=1, row=0)

start_button = Button(text="Start", background=YELLOW, fg=RED, borderwidth=0, font=(FONT_NAME, 20, "bold"),
                      command=start_clicked)

start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", background=YELLOW, fg=RED, borderwidth=0, font=(FONT_NAME, 20, "bold"),
                      command=reset_clicked)
reset_button.grid(column=2, row=2)

check_label = Label(text="️", anchor='w', width=20, background=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=2)

window.mainloop()
