"""
Given the template for a button and a label.
When the button is clicked a variable should be incremented by 1
The value of this variable should be displayed as a label when the button is
clicked.
"""
from tkinter import *

window = Tk()
count = 0


def click():
	global count
	count += 1
	label.config(text=count)


label = Label(window,
              text=count,
              font = ("arial", 20),
              fg ="white",
              bg="black")

countButton = Button(window,
                     text="Click to count",
                     command=click,
                     fg="black",
                     bg="white")

countButton.grid(row=0, column=0)
label.grid(row=1, column=0)


window.mainloop()
