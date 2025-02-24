import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)


def search():
    website_search = website_entry.get()
    try:
        with open('pass.json', 'r') as data_file:
            data = json.load(data_file)
            pass_search = data[website_search]['Password']
            mail_search = data[website_search]['Email']
    except:
        messagebox.askokcancel(title=website_search, message='No data found')
    else:
        messagebox.askokcancel(title=website_search, message=f"Email: {mail_search}, \nPassword: {pass_search}")


def random1():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pyperclip.copy(password)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)


def add_fun():
    is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"Email: {user_entry.get()} \nPassword: {pass_entry.get()} \nIs it okay?")

    new_data = {
            website_entry.get(): {
                'Email': user_entry.get(),
                'Password': pass_entry.get(),
            }
    }

    if is_ok:
        try:
            with open('pass.json') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('pass.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open('pass.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


website = Label(text='Website')
website.grid(row=1, column=0)
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)
username = Label(text='Username/Email')
username.grid(row=2, column=0)
user_entry = Entry(width=39)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, 'hiexbris@gmail.com')
password1 = Label(text='Password')
password1.grid(row=3, column=0)
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

generate = Button(text="Generate Password", command=random1)
generate.grid(row=3, column=2)
search = Button(text="Search", width=14, command=search)
search.grid(row=1, column=2)
add = Button(text="Add", command=add_fun, width=35)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()