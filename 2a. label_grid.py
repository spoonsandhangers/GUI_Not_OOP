"""
This is a basic window that closes when the cross is pressed.
It contains a label that is added to the window using grid layout.
"""
from tkinter import *

window = Tk()

label = Label(window,text ="no formatting")

# creates a label called label 1, sets the text, font, foreground colour(text) and background colour.
# relief can = RAISED OR SUNKEN this is the border.  bd is border size
# padx and pady sets space between border and text or image
label1 = Label(window,text="Hello World",
               font=('Ariel', 40, 'bold'),
               fg ='green',
               bg='black', relief=RAISED,
               bd=10,
               padx=20,
               pady=20)

label2 = Label(window,text="This is label 2",
               font=('Ariel', 10, 'bold'),
               fg ='blue',
               bg='orange', relief=RAISED,
               bd=10,
               padx=20,
               pady=20,)

label3 = Label(window,text="number 3",
               font=('Ariel', 20, 'bold'),
               fg ='blue',
               bg='orange', relief=RAISED,
               bd=10,
               padx=20,
               pady=20)

label.grid(row=0, column=0)
label1.grid(row=0, column=1)
label2.grid(row=1, column=0)
label3.grid(row=1, column=1)
window.mainloop()
