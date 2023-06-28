from tkinter import *

window = Tk()
window.minsize(height=120, width=200)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Km variable

entry = Entry(width=10)
entry.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to ")
is_equal_to_label.grid(column=0, row=1)

km_num_label = Label(text="")
km_num_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def button_click():
    km = 1.60934 * int(entry.get())
    km_num_label.config(text=str(km))


button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)












window.mainloop()