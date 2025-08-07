from tkinter import*
from tkinter import messagebox
import random
import pyperclip
import json


#generate password

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def create_password():
    list1=[random.choice(letters) for item in range (random.randint(1,6))]
    list2 =[random.choice(numbers) for item in range(random.randint(1,6))]
    list3 =[random.choice(symbols) for item in range(random.randint(1,6))]
    comprehenshion=list1 + list2 + list3
    random.shuffle(comprehenshion)
    passw=''.join(comprehenshion)
    box3.insert(0,passw)
    pyperclip.copy(passw)  #forgot this


def save_password():
    website=box1.get()
    email=box2.get()
    password=box3.get()
    new_data={website:{"Email":email, "Password": password}}
    if len(box1.get())==0 or len(box2.get())==0 or len(box3.get())==0:
        messagebox.showinfo(message="Enter value for all the fields")
        return
    check=messagebox.askyesno(message=f"This is what you've entered : \n  Website: {website}, Email : {email}, Password :{password}. Do you want to save?")
    if check:
        try:
            with open("data.json","r") as data:
                uploaded = json.load(data) if data.read().strip() else {}

        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)

        else:
            uploaded.update(new_data)
            with open("data.json", "w") as file:
                json.dump(uploaded, file, indent=4)
        finally:
            box1.delete(0,END) #FORGOT THIS FUNCTION
            box3.delete(0,END)

def look():
    website=box1.get()
    try:
        with open("data.json") as data:
            stored=json.load(data)
            if website in stored:
                email=stored[website]["Email"]
                password = stored[website]["Password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

            else:
                messagebox.showinfo(title="Not Found", message="No details found for this website.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")









#UI
screen=Tk()
screen.title("Password Manager")
canvas=Canvas(width=300, height=300)
canvas.grid(column=1, row=0) #I forgot this
exp=PhotoImage(file="logo.png")
canvas.create_image(150,150,image=exp)
website=Label(text="Website:")
website.grid(column=0,row=1)
box1=Entry(width=25)
box1.grid(column=1,row=1, columnspan=3)
box1.focus()
search=Button(text="search",command=look)
search.grid(column=3,row=1)

email=Label(text="Email:")
email.grid(column=0,row=2)
box2=Entry(width=25)
box2.grid(column=1,row=2, columnspan=3)
box2.insert(0,"abhiraj21.srivastava@gmail.com") #forgot this function
password=Label(text="Password:")
password.grid(column=0,row=3)
generate=Button(text="make password", command=create_password)
generate.grid(column=3,row=3,columnspan=2)

box3=Entry(width=25)
box3.grid(column=1,row=3, columnspan=3)

add=Button(text="add",width=25,command=save_password)
add.grid(column=1,row=4,columnspan=3)



screen.mainloop()

