import datetime
import tkinter as tk
from PIL import Image,ImageTk
win = tk.Tk()
win.geometry("620x780")
win.title(" Age Calculator APP ")
name = tk.Label(text="Name")
name.grid(column=0,row=1)
year = tk.Label(text="Year")
year.grid(column=0,row=2)
month = tk.Label(text="Month")
month.grid(column=0,row=3)
date = tk.Label(text="Date")
date.grid(column=0,row=4)
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)

def getInput():
    name = nameEntry.get()
    monkey = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    textArea = tk.Text(master=win,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer = " Hey {monkey}!!!. You are {age} years old".format(monkey=name,age=monkey.age())
    textArea.insert(tk.END,answer)
button = tk.Button(win,text="Calculate Age",command=getInput,bg="pink")
button.grid(column=1,row=5)
class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age
# image = Image.open("sam.jpg")
# image.thumbnail((300,300),Image.ANTIALIAS)
# photo = ImageTk.PhotoImage(image)
# label_image = tk.Label(image=photo)
# label_image.grid(column=1,row=0)
win.mainloop()