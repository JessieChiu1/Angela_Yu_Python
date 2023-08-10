# Angela_Yu_Python

Go to subfolder and run `py main.py` to view project for each day

## rewriting git history (removing sensitive data)
https://www.youtube.com/watch?v=Bo-8EfDpKxA&ab_channel=DanGitschooldude

## List Comprehension
`new_list = [new_item for item in list if test]`

## Dictionary Comprehension
`new_dict = {new_key:new_value for (key, value) in dict.item() if test}`

Example of dictionary list comprehension from pandas's csv file

`data = [{"Word": row[1], "Definition": row[3]} for _, row in df.iterrows()]`

## Tkinter and GUI

# Label
`my_label = tk.Label(text="I am a label", font=("Arial", 12, "bold"))`
`my_label.pack()`

`my_label["text"] = "New Text"`

I can change the text or attribute of the label like this:

`my_label.config(text="New Text")`


# Button
`def button_clicked():`
`    my_label.config(text=entry.get())`

`button = tk.Button(text="Click Me", command=button_clicked)`
`button.pack()`

# Entry

This is basically a 1 line input/text box

`entry = tk.Entry(width=60)`
`entry.insert(tk.END, "this is how you put some starting text in the entry box")`

# Text
This is MULTI line text box

`text = tk.Text(height=5, width=30)`

Put cursor in textbox on INIT

`text.focus()`

this is how you get the text in the TEXT widget, YOU HAVE TO PASS IN ARG
gets current value in textbox at line 1, character 0

`text.insert(tk.END, "This is how you put some placeholder text in the TEXT widget ")`
`text.pack()`

# Spinbox
up and down arrow that can change magnitude

`def spinbox_used():`
    `print(spinbox.get())`

notice the "from_" arg

`spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)`
`spinbox.pack()`

# Scale
scroll that can change magnitude

you can't do the .get(), have to write it like the function below to get the value

`def scale_used(value):`
`    print(value)`

`scale = tk.Scale(from_=0, to=100, command=scale_used)`
`scale.pack()`

# CheckButton
just a checkbox for on/off true/false as 1/0

`def checkbutton_used():`
`    print(checked_state.get())`

A variable defined using IntVar() function holds integer data where we can set integer data and can retrieve it as well as using getter and setter methods

These variables can be passed to various widget parameters

Once these variables get connected to widgets, the connection works both ways: if the IntVar() variable changes, the value of the widget also get updated automatically with the new value

`checked_state = tk.IntVar()`
`checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)`
`checked_state.get()`
`checkbutton.pack()`

# Radiobutton
`def radio_used():`
`    print(radio_state.get())`

In this case the IntVar() function created a variable called radio_state that can only be the value 1,2 because of the radiobutton1 and radiobutton2 that it is connected to

`radio_state = tk.IntVar()`
`radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)`
`radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)`
`radiobutton1.pack()`
`radiobutton2.pack()`

# Listbox
`def listbox_used(event):`
`    print(listbox.get(listbox.curselection()))`

`listbox = tk.Listbox(height=4)`

need a list of value for the listbox item

`fruits = ["Apple", "Orange", "Kiwi", "Pear"]`

loop through the list to INSERT the item as a tkinter listbox item

`for item in fruits:`

takes 2 argument, first WHERE to insert the item and second the item name
an also use the END to specify to insert at the end

`listbox.insert(fruits.index(item), item)`

the bind method, takes 2 arguments, 1st is the event to listen for, and 2nd is the function that will trigger

`listbox.bind("<<ListboxSelect>>", listbox_used)`
`listbox.pack()`
