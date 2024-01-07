from tkinter import *
from helpers import search_data, generate_pass, verify_beforehand

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
website_label = Label(
    text="Website:",
    fg=BLACK, bg=CREAM,
    font=(FONT_BOOKMAN, 10, "normal"),
    padx=10, pady=20
)
website_input = Entry(width=26, bg=CREAM)
website_input.focus()
search_button = Button(
    text="Search",
    bg=D_CREAM,
    width=17,
    font=(FONT_LIBRE, 8),
    command=lambda: search_data(website_input)
)
website_label.grid(column=1, row=3)
website_input.grid(column=2, row=3)
search_button.grid(column=3, row=3)

# 2nd row of field: email/username label and entry input
email_label = Label(
    text="Email/Username:",
    fg=BLACK, bg=CREAM,
    font=(FONT_BOOKMAN, 10, "normal"),
    padx=10, pady=0
)
email_input = Entry(width=45, bg=CREAM)
email_label.grid(column=1, row=4)
email_input.grid(column=2, row=4, columnspan=2)

# 3rd row of field: password label, entry input and generate button
password_label = Label(
    text="Password:",
    fg=BLACK, bg=CREAM,
    font=(FONT_BOOKMAN, 10, "normal"),
    padx=10, pady=20
)
password_input = Entry(width=26, bg=CREAM)
password_generate_button = Button(
    text="Generate",
    bg=D_CREAM,
    width=17,
    font=(FONT_LIBRE, 8),
    command=lambda: generate_pass(website_input, email_input, password_input)
)
password_label.grid(column=1, row=5)
password_input.grid(column=2, row=5)
password_generate_button.grid(column=3, row=5)

# 4th row of field: save button
save_button = Button(
    text="SAVE Password",
    bg=D_CREAM,
    width=45,
    font=(FONT_LIBRE, 8),
    command=lambda: verify_beforehand(website_input, email_input, password_input)
)
save_button.grid(column=2, row=6, columnspan=2)

# Keeps the window open
window.mainloop()
