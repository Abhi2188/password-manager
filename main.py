from tkinter import*
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters=[random.choice(letters) for letter in range(nr_letters)]
    numbers=[random.choice(numbers) for num in range(nr_numbers)]
    symbols=[random.choice(symbols) for symbol in range(nr_symbols)]
    combined=letters + numbers + symbols
    shuffled="".join(combined)
    box3.insert(0,f"{shuffled}")
    pyperclip.copy(shuffled)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = box1.get()
    email = box2.get()
    password = box3.get()
    new_data = {web: {"email": email, "password": password}}

    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(message="Oops! Make sure you haven't left any field empty")
    else:
        try:
            with open("data.json", mode="r") as data:
                stuff = json.load(data)
        except FileNotFoundError:
            with open("data.json", mode="w") as data:
                json.dump(new_data, data, indent=2)
        else:
            stuff.update(new_data)
            with open("data.json", mode="w") as data:
                json.dump(stuff, data, indent=4)
        finally:
            box1.delete(0, END)
            box3.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(height=200, width=200)
canvas.grid(column=1,row=0)
importing_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=importing_image)
website=Label(text="Website:")
website.grid(column=0,row=1)

box1= Entry(width=21)
box1.grid(column=1, row=1, columnspan=1)
box1.focus()
def find_password():
    websi=box1.get()
    try:
        with open("data.json") as data:
            ah=json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(text="file not found")
    else:
        if websi in data:

            email=data[websi]["email"]
            passwords=data[websi]["password"]
            messagebox.showinfo(message=f"{email}, {password}")
        else:

            messagebox.showinfo(text="no such website")



search=Button(text="Search", width=13,command=find_password)
search.grid(column=2, row=1)


email=Label(text="Email/Username:")
email.grid(column=0,row=2)
box2= Entry(width=35)
box2.grid(column=1, row=2, columnspan=2)
box2.insert(0,"abhiraj21.srivastava@gmail.com")
passwordd=Label(text="Password:")
passwordd.grid(column=0,row=3,columnspan=1)
box3= Entry(width=21)
box3.grid(column=1, row=3)
button1=Button(text="Generate Password", command= password)
button1.grid(column=2, row=3)
button2=Button(text="Add", width=35,command= save)
button2.grid(column=1, row=4, columnspan=2)






window.mainloop()