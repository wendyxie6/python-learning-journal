import tkinter as tk
import random
class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

def findJob():
    newJob = jobEntry.get()
    me.job = newJob
    label3.config(text=f"Job: {me.job}")
    
def quitJob():
    me.job = "Unemployee"
    label3.config(text=f"Job: {me.job}")


me = Person("Wendy", 28, "Student")

myWindow = tk.Tk()

myWindow.title("My First GUI")
myWindow.geometry("600x600")

#label
label = tk.Label(myWindow, text=f"Name: {me.name}",  font=("Helvetta, 30"))
label.pack()

label2 = tk.Label(myWindow, text=f"Age: {me.age}", font=("Ariel", 16))
label2.pack()

label3 = tk.Label(myWindow, text=f"Job: {me.job}", font=("Ariel", 16))
label3.pack()

jobEntry = tk.Entry(myWindow)
jobEntry.pack(pady=20)

button = tk.Button(myWindow, text = "Find a job", command=findJob)
button.pack(pady=20)

button2 = tk.Button(myWindow, text = "Quit job", command=quitJob)
button2.pack(pady=20)
    
myWindow.mainloop()