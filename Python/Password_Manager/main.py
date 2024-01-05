from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from string import ascii_letters, digits, punctuation
from pyperclip import copy

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
    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()

    # If any field is empty, give error
    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showerror(title="Field Error!", message="Storages are not cheap and computation power also takes "
                                                           "maintenance. Please leave no field empty!")
    else:
        # If not, ask user if details are good to go, and save to file
        if messagebox.askokcancel(title=f"Save for {website_data}",
                                  message=f"Email: {email_data}\nPassword: {password_data}\n"
                                          f"\nPress Ok to proceed save, Cancel to check again!"):
            save_to_file(website_data, email_data, password_data)


def save_to_file(website, email, password):
    """Saves the user details to file and clears input fields"""
    with open("password_data.txt", "a+") as data_file:
        data_file.seek(0)
        index = len(data_file.readlines()) + 1
        data_file.write(f"{index}. {website} | {email} | {password} \n")

    website_input.delete(0, END)
    email_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window settings
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50, bg=CREAM)

# Image canvas
canvas = Canvas(width=200, height=200, bg=CREAM, highlightthickness=0)
bg_image = PhotoImage(file=LOCK_IMAGE)
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=2, row=1)

# 1st row of field: website label and entry input
website_label = Label(text="Website:", fg=BLACK, bg=CREAM, font=(FONT_BOOKMAN, 10, "normal"), padx=10, pady=20)
website_input = Entry(width=45, bg=CREAM)
website_label.grid(column=1, row=3)
website_input.grid(column=2, row=3, columnspan=2)
website_input.focus()

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
