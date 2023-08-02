from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am a label", font=("Arial", 12, "bold"))
my_label.pack()


# I can change the text or attribute of the label like this:
# my_label["text"] = "New Text"
# my_label.config(text="New Text")


# Button

def button_clicked():
    my_label.config(text=entry.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
# This is basically a 1 line input/text box

entry = Entry(width=60)
entry.insert(END, "this is how you put some starting text in the entry box")
# this is how you get the text in the input box
# print(entry.get())
entry.pack()

# Text
# This is MULTI line text box
text = Text(height=5, width=30)
# Put cursor in textbox on INIT
text.focus()
text.insert(END, "This is how you put some placeholder text in the TEXT widget ")
# this is how you get the text in the TEXT widget, YOU HAVE TO PASS IN ARG
# gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
# up and down arrow that can change magnitude
def spinbox_used():
    # get value of spinbox
    print(spinbox.get())


# notice the "from_" arg
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# scroll that can change magnitude
# you can't do the .get(), have to write it like the function below to get the value
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# CheckButton
# just a checkbox for on/off true/false as 1/0
def checkbutton_used():
    # print the STATE of the checkbutton
    print(checked_state.get())


# A variable defined using IntVar() function holds integer data where we can set integer data and can retrieve it as well as using getter and setter methods
# These variables can be passed to various widget parameters
# Once these variables get connected to widgets, the connection works both ways: if the IntVar() variable changes, the value of the widget also get updated automatically with the new value
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# In this case the IntVar() function created a variable called radio_state that can only be the value 1,2 because of the radiobutton1 and radiobutton2 that it is connected to
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option1", value=2, variable=radio_state, command=radio_used)
# Noticed that we need to pack BOTH buttons even though we thought of them as a single widget
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
# need a list of value for the listbox item
fruits = ["Apple", "Orange", "Kiwi", "Pear"]
# loop through the list to INSERT the item as a tkinter listbox item
for item in fruits:
    # takes 2 argument, first WHERE to insert the item and second the item name
    # Can also use the END to specify to insert at the end
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
