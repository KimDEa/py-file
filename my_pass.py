from tkinter import *
from datetime import datetime
import random
import string
import json
import os

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

my_img = PhotoImage(file='/Users/dh/py_file/udemy/logo.png')
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=my_img)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')

name_label = Label(text="Email/Username:")
name_label.grid(row=2, column=0)
name_entry = Entry(width=35)
name_entry.grid(row=2, column=1, columnspan=2, sticky='w')

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='w')

info_label = Label(text="", font=('Arial', 10))
info_label.grid(row=5, column=0, columnspan=3)

password_example = string.ascii_letters + string.digits + string.punctuation #All alphabet with upper, lower cases and numbers

def generate_password_clicked():
    password_ex = [random.choice(password_example) for i in range(12)] #List comprehension
    password_join = "".join(password_ex) #convert list to string
    password_entry.delete(0, END)
    password_entry.insert(0, password_join)

def clear_placeholder(event):
    if password_entry.get() == "Please enter a password.":
        password_entry.delete(0, END)
        password_entry.config(fg="black")

    elif name_entry.get() == "Please enter a email/username.":
        name_entry.delete(0, END)
        name_entry.config(fg="black")

    elif website_entry.get() == "Please enter a website.":
        website_entry.delete(0, END)
        website_entry.config(fg="black")

password_entry.bind("<Button-1>", clear_placeholder)
name_entry.bind("<Button-1>", clear_placeholder)
website_entry.bind("<Button-1>", clear_placeholder)

def new_window():
    window_info = Toplevel()
    window_info.title("myPass")
    window_info.config(padx=15, pady=15)

    label_info = Label(window_info, text=f"🌐 Website: {website_entry.get()}\n 👤 Email/Username: {name_entry.get()}\n 🔑 Password: {password_entry.get()}\n Is it ok to save?", font=('Arial', 10))
    label_info.grid(row=0, column=0, columnspan=3)

    def hit_ok():
        button_yes.grid_forget()
        button_no.grid_forget()

        website = website_entry.get()
        name = name_entry.get()
        password = password_entry.get()
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_data = {
            website: {
                "email/username": name,
                "password": password,
                "time": time
            }
        }

        label_info.config(text=f"Saved on /Users/dh/py_file/my_pass.json\n{time}")

        try:
            with open("/Users/dh/py_file/my_pass.json", mode="r") as file:
                #Reading old data.
                old_data = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            old_data = new_data

        else:
            #Updating old data with new_data.
            old_data.update(new_data)

        finally:
            with open("/Users/dh/py_file/my_pass.json", mode="w") as file:
                #Saving updated data.
                json.dump(old_data, file, indent=4)

        website_entry.delete(0, END)
        name_entry.delete(0, END)
        password_entry.delete(0, END)

        window.after(1500, lambda: window_info.destroy())

    button_yes = Button(window_info, text="Yes", command=hit_ok)
    button_yes.grid(row=1, column=0, columnspan=2, sticky="w")
    button_no = Button(window_info, text="No", command=window_info.destroy)
    button_no.grid(row=1, column=2, columnspan=2, sticky="e")

def overwrite_window():
    window_overwrite = Toplevel()
    window_overwrite.title("myPass")
    window_overwrite.config(padx=15, pady=15)

    label_overwrite = Label(window_overwrite, text="", font=('Arial', 10, 'bold'))
    label_overwrite.grid(row=0, column=0, columnspan=3)

    def ok():
        window_overwrite.destroy()
        return new_window()
    
    try:
        with open("/Users/dh/py_file/my_pass.json", mode="r") as file:
            overwrite_data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        label_overwrite.config(text="There's no saved data in\n /Users/dh/py_file/my_pass.json")
        window_overwrite.after(2000, lambda: label_overwrite.config(text=""))

    else:
        website_get = website_entry.get()
        is_overwrite = {website: info for website, info in overwrite_data.items() if website == website_get}
        if is_overwrite:
            label_overwrite.config(text="This website is already registered. Would you like to overwrite it?")
        else:
            window_overwrite.destroy()
            return new_window()
    
    button_yes = Button(window_overwrite, text="Yes", command=ok)
    button_yes.grid(row=1, column=0, columnspan=2, sticky="w")
    button_no = Button(window_overwrite, text="No", command=window_overwrite.destroy)
    button_no.grid(row=1, column=2, columnspan=2, sticky="e")

def add_clicked():
    conditions = [password_entry.get(), name_entry.get(), website_entry.get()]
    conditions_message = [
        "Please enter a password.",
        "Please enter a email/username.",
        "Please enter a website."
    ]
    if password_entry.get() == "":
        password_entry.delete(0, END)
        password_entry.config(fg="gray")
        password_entry.insert(END, conditions_message[0])

    if name_entry.get() == "":
        name_entry.delete(0, END)
        name_entry.config(fg="gray")
        name_entry.insert(END, conditions_message[1])

    if website_entry.get() == "":
        website_entry.delete(0, END)
        website_entry.config(fg="gray")
        website_entry.insert(END, conditions_message[2])

    if len(password_entry.get()) > 12 or len(password_entry.get()) < 12 and len(password_entry.get()) != 0:
        info_label.config(text="Password must be 12 characters long.")
        window.after(2000, lambda: info_label.config(text=""))
        return
    
    if conditions and password_entry.get() != conditions_message[0] and name_entry.get() != conditions_message[1] and website_entry.get() != conditions_message[2]:
        overwrite_window()

def search_clicked():
    search_info_window = Toplevel()
    search_info_window.title("MyPass Search")
    search_info_window.config(padx=15, pady=15)

    search_info = Label(search_info_window, text="", font=('Arial', 10, 'bold'))
    search_info.grid(row=0, column=0, columnspan=3, sticky="w")
    search_info_button = Button(search_info_window, text="Ok", font=('Arial', 10), command=search_info_window.destroy)
    search_info_button.grid(row=1, column=0, columnspan=2)

    def copy_pwd():
        search_info_window.clipboard_clear()
        search_info_window.clipboard_append(pwd_text)
        copy_button.config(text="Copied!", fg="green")
        search_info_window.after(1500, lambda: copy_button.config(text="Copy", fg="black"))
    
    copy_button = Button(search_info_window, text="Copy", font=('Arial', 9), command=copy_pwd)
    copy_button.grid(row=1, column=2)

    try:
        with open("/Users/dh/py_file/my_pass.json", mode="r") as file:
            vault_data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        search_info.config(text="There's no saved data in\n /Users/dh/py_file/my_pass.json")
        search_info_window.after(2000, lambda: search_info.config(text=""))

    else:
        search_w = website_entry.get()
        search_n = name_entry.get()

        search_dict = {website: info for website, info in vault_data.items() if info["email/username"] == search_n and website == search_w}

        if search_dict:
            actual_info = search_dict[search_w]
            pwd_text = actual_info["password"]
            display_text=(
                f"🌐 Website: {search_w}\n"
                f"👤 Email/Username: {actual_info["email/username"]}\n"
                f"🔑 Password: {actual_info["password"]}\n"
                f"📅 Added time: {actual_info["time"]}"
            )
        else:
            display_text = "Can't not found any info, Please try again."
            copy_button.grid_forget()
            search_info_button.grid(row=1, column=0, columnspan=3)

    finally:
        search_info.config(text=f"{display_text}")

generate_password_button = Button(text="Generate Password", command=generate_password_clicked, font=('Arial', 10))
generate_password_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", font=('Arial', 10), width=20, command=add_clicked)
add_button.grid(row=4, column=1, sticky='w')

search_button = Button(text="Search", font=('Arial', 10), command=search_clicked)
search_button.grid(row=4, column=2, sticky='w')

window.mainloop()