"""
A guided rock paper scissors project
Students given a template with comments explaining what they need to add.
Hints and code along for lower abilities.
Challenge and extensions - using more advanced formatting to make the
game look better.
Also displaying the computers choice as a picture.
"""

from tkinter import *
from random import choice

window = Tk()
window.title("Rock, Paper, Scissors")

# create images
rock = PhotoImage(file='rock.PNG')
paper = PhotoImage(file='paper.png')
scissors = PhotoImage(file='scissors.PNG')


# a subroutine that displays the users choice
def play():
	choices = ["rock", "paper", "scissors"]
	comp_choice = choice(choices)
	titleText = "Computer chooses " + comp_choice
	lbl_title.config(text=titleText)

	if chosen.get() == "rock":
		player1.config(image=rock)
		if comp_choice == "rock":
			lbl_result.config(text="It's a draw",
			                  font=("arial",20))
		elif comp_choice == "paper":
			lbl_result.config(text="Paper wraps rock!\nComputer wins",
			                  font=("arial",20))
		elif comp_choice == "scissors":
			lbl_result.config(text="Rock smashes scissors!\nPlayer wins",
			                  font=("arial",20))

	elif chosen.get() == "paper":
		player1.config(image=paper)
		if comp_choice == "paper":
			lbl_result.config(text="It's a draw",
			                  font=("arial", 20))
		elif comp_choice == "rock":
			lbl_result.config(text="Paper wraps rock!\nPlayer wins",
			                  font=("arial",20))
		elif comp_choice == "scissors":
			lbl_result.config(text="Scissors cut paper!\nComputer wins",
			                  font=("arial",20))

	elif chosen.get() == "scissors":
		player1.config(image=scissors)
		if comp_choice == "scissors":
			lbl_result.config(text="It's a draw",
			                  font=("arial", 20))
		elif comp_choice == "rock":
			lbl_result.config(text="Rock smashes scissors!\nComputer wins",
			                  font=("arial",20))
		elif comp_choice == "paper":
			lbl_result.config(text="Scissors cut paper!\nPlayer wins",
			                  font=("arial",20))


# Create title label that changes to show computer choice
lbl_title = Label(window, text= "Rock paper Scissors game", font=("arial", 25))

# create label to display the images
player1 = Label(window)

# create label to display game result
lbl_result = Label(window)

# create a variable to store the choice from the drop down menu.
chosen = StringVar()
chosen.set("rock")

# create drop down list with choice for player
drp_playerchoice = OptionMenu(window, chosen, "rock", "paper", "scissors")

# create button to play choice
btn_play = Button(window,
                  text="Play this choice",
                  command=play,
                  font=("arial",15),
                  )


lbl_title.grid(row=0, column=1)
player1.grid(row=1,column=1)
lbl_result.grid(row=4,column=1)
btn_play.grid(row=3,column=1)
drp_playerchoice.grid(row=2,column=1)


window.mainloop()
