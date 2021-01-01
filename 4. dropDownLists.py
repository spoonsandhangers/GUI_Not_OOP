from tkinter import *

window = Tk()

def show():
	myLabel = Label(window,text=choice.get()).pack()

choice = StringVar()
choice.set("Python")

drop = OptionMenu(window, choice, "Python", "Java", "C++", "Javascript", "PHP", "C#")
myButton = Button(window, text="Show selection", command=show)

drop.pack()
myButton.pack()

window.mainloop()
