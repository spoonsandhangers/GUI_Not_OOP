"""
A button that when clicked displays a label with a picture and text
The button also prints out a count of the amount of times it has been clicked

A second button is added to change the colour of the first button when clicked
This shows how the config method can be used.
"""
from tkinter import *

window = Tk() # creates an instance of a window

window.geometry("500x600") # sets the size of the window must be in quotes with x in the middle
window.title("My Window") # title of window.

window.config(background="black") # instead of the name you can use a hex value from a colour picker hex values must begin with #

###### buttons #######

# a variable declared outside of a function is a global variable
count = 0


def click():
    # this tells the function to use the global variable count
    global count
    count += 1
    print(count)
    button3.pack()
    label1.pack(side=BOTTOM)



def change():
	button1.config(bg="white")
	button1.config(fg="purple")
	button3.config(bg="orange")
	button2.pack_forget()


def forgetMe():
	label1.pack_forget()


# state = DISABLED OR ACTIVE
button1 = Button(window,
                 text="click here",
                 command=click,
                 font=('Comic sans', 15),
                 fg='#0066FF',
                 bg='yellow',
                 activeforeground='#0066FF',
                 activebackground='yellow')

button2 = Button(window,
                 text="Change Button Colours",
                 command=change,
                 font=("comic sans", 15))

button3 = Button(window,
                 text="Bye bye",
                 command=forgetMe,
                 font=("helvetica",15))


button1.pack()
button2.pack(side=BOTTOM)



###### a label ######## an area widget that contains text or an image

# create a photo image to add to the label

photo = PhotoImage(file='thumb_up.PNG')

# creates a label called label 1, sets the text, font, foreground colour(text) and background colour.
# relief can = RAISED OR SUNKEN this is the border.  bd is border size
# padx and pady sets space between border and text or image
label1 = Label(window,text="Hello World",
               font=('Ariel', 40, 'bold'),
               fg ='green',
               bg='black', relief=RAISED,
               bd=10,
               padx=20,
               pady=5,
               image=photo,
               compound='bottom')

 # puts the label on the frame.
#label1.place(x=0,y=0) # instead of pack use place to put the label in a specific place.


window.mainloop() # displays the window listen for events
