"""
Flash card project
Students should construct a flash card GUI
This should contain flash cards about Python
level 1 - at least 3 flash cards - 2 labels and a button
level 2 - at least 5 flash cards - 2 labels, a button and a drop down list
Level 3 - at least 5 flash cards - 2 labels, a button, a drop down list and
			a way of checking if answers are correct and keeping score.

extensions - saving the score to a text file to load up next time.
			- advanced formatting
"""
from tkinter import *
from random import choice

window = Tk()


# create a variable for the drop down menu choice
# then set the default value.
response = StringVar()
response.set("int")
# declare theQuestion as a variable
theQuestion = StringVar()
theQuestion.set("What data type is this value\n54.0")
def theQuestions():
		questions =["What data type is this value\n100",
		            "What data type is this value\n'09873676253'",
	                "What data type is this value\nTrue",
	                "What data type is this value\n'True'",
	                "What data type is this value\n234",
	                "What data type is this value\n'hello world'",
	                "What data type is this value\nFalse"]

		for i in questions:
			yield i

aQuestion = theQuestions()

def show():
	global aQuestion
	#theQuestion.set(choice(questions))
	lbl_question.config(text=next(aQuestion))

def submit():
	pass

# drop down list of answers
drp_answers = OptionMenu(window,
                         response,
                         "int",
                         "float",
                         "string",
                         "boolean")


lbl_title = Label(window,
                  text="Python Flash Cards",
                  font=("comic sans",20))

lbl_question = Label(window,
                     text=theQuestion.get(),
                     font=("comic sans", 20)
                     )

btn_showCard = Button(window,
                      text="Show a card",
                      font=("comic sans", 20),
                      command=show)

btn_submitAnswer = Button(window,text="Submit answer",font=("comic sans", 20),command=submit)

lbl_title.grid(row=0, column=1)
lbl_question.grid(row=1, column=1)
drp_answers.grid(row=1, column=2)
btn_showCard.grid(row=2, column=1)
btn_submitAnswer.grid(row=2, column=2)

window.mainloop()
