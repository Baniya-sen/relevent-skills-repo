from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from string import ascii_letters, digits, punctuation
from pyperclip import copy
import json

# CONSTANTS
WHITE = "white"
CREAM = "#FFFFEC"
D_CREAM = "#fcfce6"
BLACK = "black"
GREEN = "#597E52"
FONT_BOOKMAN = "Bookman Old Style"
FONT_LIBRE = "Libre Baskerville"
FONT_LISU = "LiSu"
FONT_CONSOLE = "Lucida Console"
FONT_SANS = "Lucida Sans"
LOCK_IMAGE = "logo.png"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    """Generates a random password based on website name and email provided"""
    # Generate a list with 8-10 random letters, 2-4 digits and 2-4 punctuations
    random_char_list = [choice(ascii_letters) for _ in range(randint(8, 10))]
    random_char_list += [choice(digits) for _ in range(randint(2, 4))]
    random_char_list += [choice(punctuation) for _ in range(randint(2, 4))]
    shuffle(random_char_list)

    # Get the data from website and email field
    website_data = website_input.get()
    email_data = email_input.get()

    # If website name and email provided, adds a portion of both to password
    if len(website_data) != 0 or len(email_data) != 0:
        random_char_list.append(
            f"?{website_data[:int(len(website_data) / 4)]}={email_data[:int(len(website_data) / 4)]}")

    # Creates a password string, add to password field and copy to clipboard
    random_password = ''.join(random_char_list)
    password_input.delete(0, END)
    password_input.insert(0, random_password)
    copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def verify_beforehand():
    """Prompt user to verify details before storing to file-system"""
    website_data = website_input.get().lower()
    email_data = email_input.get()
    password_data = password_input.get()

    # If any field is empty, give error
    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showerror(title="Field Error!", message="Storages are not cheap and computation power also takes "
                                                           "maintenance. Please leave no field empty!")
    else:
        # If not, save to json file
        save_to_file(website_data, email_data, password_data)


def save_to_file(website, email, password):
    """Saves the user details to JSON file and clears input fields"""
    # JSON data
    password_entry = {
        website: {
            "Email/Username": email,
            "Password": password,
        }
    }
    # Porting data to file, if exists, if not, then create new file to store data
    try:
        with open("password_data.json", "r+") as data_file:
            # If not data in file, or data is corrupted json, then data = empty dict
            try:
                json_data = json.load(data_file)
            except json.decoder.JSONDecodeError:
                json_data = {}
            # We'll update json file with new entry data
            json_data.update(password_entry)
            data_file.seek(0)
            json.dump(json_data, data_file, indent=4)
    except FileNotFoundError:
        with open("password_data.json", "w") as data_file:
            json.dump(password_entry, data_file, indent=4)
    finally:
        # Clear entry input fields
        website_input.delete(0, END)
        email_input.delete(0, END)
        password_input.delete(0, END)
        website_input.focus()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search_data():
    """Searches password with website name from json file"""
    website_query = website_input.get().lower()
    # If website field is empty, yell at user
    if len(website_query) == 0:
        messagebox.showerror(title="Fill required field!",
                             message="Please enter Website name for which email and password you want.")
    else:
        try:
            with open("password_data.json", "r") as data_file:
                try:
                    password_data = json.load(data_file)
                except json.decoder.JSONDecodeError:
                    messagebox.showerror(title="Read Error!",
                                         message="The data on the JSON file is corrupted or doesn't exists!")
        except FileNotFoundError:
            messagebox.showerror(title="File Not Found!",
                                 message="The is not such file on disk that contains password data")
        else:
            # If website is indeed stored in data, then show email and password in a alert box
            if website_query in password_data:
                email_from_file = password_data[website_query]["Email/Username"]
                password_from_file = password_data[website_query]["Password"]
                copy(password_from_file)
                messagebox.showinfo(title="Password data",
                                    message=f"Email: {email_from_file}\nPassword: {password_from_file}\n"
                                            f"(Password saved to clipboard!)")
            else:
                messagebox.showerror(title="No data found!",
                                     message=f'There is no such website "{website_query}" found in data.')


# ---------------------------- UI SETUP ------------------------------- #
# Window settings
window = Tk()
window.title("Password Manager")
window.config(padx=110, pady=50, bg=CREAM)

# Image canvas
canvas = Canvas(width=200, height=200, bg=CREAM, highlightthickness=0)
bg_image = PhotoImage(file=LOCK_IMAGE)
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=2, row=1)

# 1st row of field: website label and entry input
website_label = Label(text="Website:", fg=BLACK, bg=CREAM, font=(FONT_BOOKMAN, 10, "normal"), padx=10, pady=20)
website_input = Entry(width=26, bg=CREAM)
website_input.focus()
search_button = Button(text="Search", bg=D_CREAM, width=17, font=(FONT_LIBRE, 8), command=search_data)
website_label.grid(column=1, row=3)
website_input.grid(column=2, row=3)
search_button.grid(column=3, row=3)

# 2nd row of field: email/username label and entry input
email_label = Label(text="Email/Username:", fg=BLACK, bg=CREAM, font=(FONT_BOOKMAN, 10, "normal"), padx=10, pady=0)
email_input = Entry(width=45, bg=CREAM)
email_label.grid(column=1, row=4)
email_input.grid(column=2, row=4, columnspan=2)

# 3rd row of field: password label, entry input and generate button
password_label = Label(text="Password:", fg=BLACK, bg=CREAM, font=(FONT_BOOKMAN, 10, "normal"), padx=10, pady=20)
password_input = Entry(width=26, bg=CREAM)
password_generate_button = Button(text="Generate", bg=D_CREAM, width=17, font=(FONT_LIBRE, 8), command=generate_pass)
password_label.grid(column=1, row=5)
password_input.grid(column=2, row=5)
password_generate_button.grid(column=3, row=5)

# 4th row of field: save button
save_button = Button(text="SAVE Password", bg=D_CREAM, width=45, font=(FONT_LIBRE, 8), command=verify_beforehand)
save_button.grid(column=2, row=6, columnspan=2)

window.mainloop()
