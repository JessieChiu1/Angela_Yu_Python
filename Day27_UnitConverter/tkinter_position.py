from tkinter import *

# window setup
window = Tk()
window.title("widget placement tutorial")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.place(x=0,y=0)
my_label.grid(column=0, row=0)


# Button
def button_clicked():
    print("button is clicked")


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
entry = Entry(width=30)
entry.insert(END, "Some placeholder text")
entry.grid(column=2, row=2)

# There are 3 main layout manager pack(), place(), grid()
# Pack(self?)
    # By default, pack() will go from center top to center bottom()
    # You can change the align by using 'side=left' or 'side=right'
    # This will align the widget from left center to right center or vice versa
# Place(x, y)
    # All about precise positioning
# grid(column, row)
    # This think of the whole window as a grid and put the widget according to the grid column and row structure
    # You CANNOT mix up grid and place in the same tkinter window


window.mainloop()