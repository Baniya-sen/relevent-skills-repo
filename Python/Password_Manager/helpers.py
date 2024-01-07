from tkinter import messagebox, END
from random import choice, randint, shuffle
from string import ascii_letters, digits, punctuation
from pyperclip import copy
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass(website_textfield, email_textfield, password_textfield):
    """Generates a random password based on website name and email provided"""
    # Generate a list with 8-10 random letters, 2-4 digits and 2-4 punctuations
    random_char_list = [choice(ascii_letters) for _ in range(randint(8, 10))]
    random_char_list += [choice(digits) for _ in range(randint(2, 4))]
    random_char_list += [choice(punctuation) for _ in range(randint(2, 4))]
    shuffle(random_char_list)

    # Get the data from website and email field
    website_data = website_textfield.get()
    email_data = email_textfield.get()

    # If website name and email provided, adds a portion of both to password
    if len(website_data) != 0 or len(email_data) != 0:
        random_char_list.append(
            f"?{website_data[:int(len(website_data) / 4)]}={email_data[:int(len(website_data) / 4)]}")

    # Creates a password string, add to password field and copy to clipboard
    random_password = ''.join(random_char_list)
    password_textfield.delete(0, END)
    password_textfield.insert(0, random_password)
    copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def verify_beforehand(website_textfield, email_textfield, password_textfield):
    """Prompt user to verify details before storing to file-system"""
    website_data = website_textfield.get().lower()
    email_data = email_textfield.get()
    password_data = cipher_data(password_textfield.get(), "encrypt")  # Encrypt password before storing

    # If any field is empty, give error
    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showerror(title="Field Error!", message="Storages are not cheap and computation power also takes "
                                                           "maintenance. Please leave no field empty!")
    else:
        # If not, save to json file
        save_to_file(website_textfield, email_textfield, password_textfield, password_data)


def save_to_file(website_textfield, email_textfield, password_textfield, ciphered_password):
    """Saves the user details to JSON file and clears input fields"""
    # JSON data
    password_entry = {
        website_textfield.get().lower(): {
            "Email/Username": email_textfield.get(),
            "Password": ciphered_password,
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
        website_textfield.delete(0, END)
        email_textfield.delete(0, END)
        password_textfield.delete(0, END)
        password_textfield.focus()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search_data(website_textfield):
    """Searches password with website name from json file"""
    website_query = website_textfield.get().lower()
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
            # If website is indeed stored in data, then show email and password in alert box
            if website_query in password_data:
                email_from_file = password_data[website_query]["Email/Username"]
                password_from_file = password_data[website_query]["Password"]
                password_from_file = cipher_data(password_from_file, "decrypt")  # Decrypt password
                copy(password_from_file)

                messagebox.showinfo(title="Password data",
                                    message=f"Email: {email_from_file}\nPassword: {password_from_file}\n"
                                            f"(Password saved to clipboard!)")
            else:
                messagebox.showerror(title="No data found!",
                                     message=f'There is no such website "{website_query}" found in data.')


# ---------------------------- PASSWORD ENCRYPTOR ------------------------------- #
def cipher_data(plaintext, method):
    """Performs encryption or decryption on password with define method"""
    cipher_text = ""
    # A string with all alphabetic letters, digits and punctuations
    all_letters = ascii_letters + digits + punctuation
    # A key to shift letters through
    key = -int(plaintext[-1]) if method == "decrypt" else int(choice(digits))

    for char in plaintext:
        cipher_text += all_letters[(all_letters.index(char) + key) % len(all_letters)]

    # If encryption, add decryption key to end of password
    if method == "encrypt":
        return cipher_text + str(key)
    else:
        return cipher_text[0:-1]
