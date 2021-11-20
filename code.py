from tkinter import *
import random


def game(player):
    select = [1, 2, 3]
    comp_choice = random.choice(select)
    if player == 1:
        canvas.itemconfig(player_default_img, image=rock_p)
    elif player == 2:
        canvas.itemconfig(player_default_img, image=paper_p)
    else:
        canvas.itemconfig(player_default_img, image=scissors_p)

    if comp_choice == 1:
        canvas.itemconfig(computer_default_img, image=rock_p)
    elif comp_choice == 2:
        canvas.itemconfig(computer_default_img, image=paper_p)
    else:
        canvas.itemconfig(computer_default_img, image=scissors_p)
    if player == comp_choice:
        canvas.itemconfig(result_text, text="Result:- Draw")
    elif (player == 1 and comp_choice == 2) or (player == 2 and comp_choice == 1) or (player == 3 and comp_choice == 2):
        canvas.itemconfig(result_text, text="Result:- You Win")
    else:
        canvas.itemconfig(result_text, text="Result:- You Loss")


window = Tk()
window.title("Rock, Paper, Scissors")
window.config(padx=25, pady=25)
canvas = Canvas(width=800, height=650)
canvas.grid(row=0, column=0)
# ----------Images------------------
paper_p = PhotoImage(file="PICS/paper.jpeg")
rock_p = PhotoImage(file="PICS/rock.jpeg")
scissors_p = PhotoImage(file="PICS/scissor.jpeg")
default_p = PhotoImage(file="PICS/default.jpeg")
computer_default_img = canvas.create_image(600, 250, image=default_p)
player_default_img = canvas.create_image(150, 250, image=default_p)

choice_i = PhotoImage(file="PICS/Selection.jpg")
player_choice_img = canvas.create_image(150, 525, image=choice_i)
computer_choice_img = canvas.create_image(650, 525, image=choice_i)

# ----------Labels----------------
player_text = canvas.create_text(100, 20, text="PLAYER", font=('Algerian', 40))
computer_text = canvas.create_text(670, 20, text="COMPUTER", font=('Algerian', 40))
vs_text = canvas.create_text(390, 300, text="V/S", font=('Algerian', 35))
result_text = canvas.create_text(390, 625, text="", font=('Algerian', 25))
# ----------Buttons----------------

rock_button = Button(text="Rock", command=lambda: game(1))
rock_button.place(x=25, y=560)
paper_button = Button(text="Paper", command=lambda: game(2))
paper_button.place(x=125, y=560)
scissors_button = Button(text="Scissors", command=lambda: game(3))
scissors_button.place(x=227, y=560)
window.mainloop()
