from tkinter import *

window = Tk()

# create the photo images to add to the labels
pythonpic = PhotoImage(file='pythonIcon.PNG')
javapic = PhotoImage(file='javaicon.PNG')
cpluspic = PhotoImage(file='C++Icon.PNG')
javascriptpic = PhotoImage(file='javascripticon.PNG')
phppic = PhotoImage(file='phpicon.PNG')
csharppic = PhotoImage(file='csharpicon.PNG')


# subroutine that runs when myButton is pressed
def show():
	myLabel.config(text=choice.get())
	if choice.get() == "Python":
		myLabel.config(image=pythonpic, compound=BOTTOM)
	elif choice.get() == "Java":
		myLabel.config(image=javapic, compound=BOTTOM)
	elif choice.get() == "C++":
		myLabel.config(image=cpluspic, compound=BOTTOM)
	elif choice.get() == "Javascript":
		myLabel.config(image=javascriptpic, compound=BOTTOM)
	elif choice.get() == "PHP":
		myLabel.config(image=phppic, compound=BOTTOM)
	elif choice.get() == "C#":
		myLabel.config(image=csharppic, compound=BOTTOM)


# creates variable used in drop down menu
choice = StringVar()
choice.set("Python")

# declare all the widgets and their parameters.
drop = OptionMenu(window, choice, "Python", "Java", "C++", "Javascript", "PHP", "C#")
myButton = Button(window, text="Show selection", command=show)
myLabel = Label(window)

# add the widgets to the window.
drop.pack()
myButton.pack()
myLabel.pack()

# run window and listen for events.
window.mainloop()
