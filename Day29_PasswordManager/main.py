import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# json.dump() to write, json.load() to read, json.update() to update
import json

GREEN = "#90EE91"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
char_list = letters + numbers + symbols

# ============
# Window Setup
# ============
window = Tk()
window.minsize(width=400, height=350)
window.title("Password Manager")
window.config(padx=20, pady=20)

# ============
# Canvas setup
# ============

canvas = Canvas(width=400, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(200, 100, image=photo)
canvas.grid(column=0, row=0, columnspan=3)


# ==============
# Add login info
# ==============
# When using the json.dump() always use the option indent=4 to add 4 space for any tab to format file


def write_to_file():
    website = website_entry.get()
    username = username_entry.get()
    pw = pw_entry.get()

    # The data you dump into the JSON should be a dictionary
    new_data = {
        website: {
            "email": username,
            "password": pw,
        }
    }
    # check if any of the field is empty
    if website == "" or username == "" or pw == "":
        messagebox.showerror(title="Error", message="One or more field are empty.")
    else:
        try:
            with open("loginInfo.json", mode="r") as file:
                # Reading the old data
                data = json.load(file)
        except FileNotFoundError:
            with open("loginInfo.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            # If you don't use the json.update() the new_data won't be added to the dictionary properly
            data.update(new_data)
            with open("loginInfo.json", mode="w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            # delete what the user entered if we add the info to our file
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            pw_entry.delete(0, END)


# =====================
# Search for login info
# =====================

def search():
    try:
        website = website_entry.get()
        with open("loginInfo.json", mode="r") as file:
            data = json.load(file)
            username = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"Login Info for {website}", message=f"Email/Username: {username}\nPassword: "
                                                                           f"{password}")
    except KeyError:
        messagebox.showerror(title="Website not found", message="There is no login information for this website")


# ==================
# Password generator
# ==================

def generate_pw():
    chars = []
    pw_length = random.randint(10, 20)
    for _ in range(0, pw_length):
        chars.append(random.choice(char_list))
    pw = ''.join(chars)
    pw_entry.delete(0, END)
    pw_entry.insert(0, pw)
    pyperclip.copy(pw)


# =============
# Widgets setup
# =============

# website entry field
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=20)
website_entry.grid(column=1, row=1, pady=5)
website_entry.focus()

# Search for a website button
search_button = Button(text="Search", bg=GREEN, fg="white", borderwidth=0, width=14, command=search)
search_button.grid(column=2, row=1, pady=5)

# email/username
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_entry = Entry(width=42)
username_entry.grid(column=1, row=2, columnspan=2, pady=5)

# password
pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)
pw_entry = Entry(width=20)
pw_entry.grid(column=1, row=3)
pw_generate_button = Button(text="Generate Password", bg=GREEN, fg="white", borderwidth=0, command=generate_pw)
pw_generate_button.grid(column=2, row=3, pady=5)

# Add button
add_button = Button(text="Add", width=36, bg=GREEN, fg="white", borderwidth=0, command=write_to_file)
add_button.grid(column=1, row=4, columnspan=2, pady=5)

window.mainloop()
