import tkinter as tk

import hangman
from hangman import Hangman

# Top level window
frame = tk.Tk()
frame.title("Hangman")
frame.geometry('800x400')


# Function for getting Input
# from textbox and printing it
# at label widget

def new_game():
    global game

    game = Hangman()
    hidden_word_label.config(text=game.get_display())
    message_label.config(text=f"Enter a letter")
    button.config(text="Guess a letter", command=handle_click)


def draw_gallows(game):
    canvas.create_line(45, 10, 45, 2, width=2)
    canvas.create_line(45, 2, 2, 2, width=2)
    canvas.create_line(2, 2, 2, 230, width=2)
    canvas.create_line(2, 230, 100, 230, width=2)

    if game.get_number_of_incorrect_guesses() >= 1:
        canvas.create_oval(10, 10, 80, 80, outline="black", fill="white", width=2)
    if game.get_number_of_incorrect_guesses() >= 2:
        canvas.create_line(45, 80, 45, 180, width=2)
    if game.get_number_of_incorrect_guesses() >= 3:
        canvas.create_line(45, 110, 5, 130, width=2)
    if game.get_number_of_incorrect_guesses() >= 4:
        canvas.create_line(45, 110, 85, 130, width=2)
    if game.get_number_of_incorrect_guesses() >= 5:
        canvas.create_line(45, 180, 5, 220, width=2)
    if game.get_number_of_incorrect_guesses() >= 6:
        canvas.create_line(45, 180, 85, 220, width=2)


def handle_click():
    global game

    letter_guessed = inputtxt.get(1.0, "end-1c").upper()
    if len(letter_guessed) != 1:
        message_label.config(text="Please enter a single letter")
    else:
        game.guess_letter(letter_guessed)

        if game.game_over():
            message_label.config(text=f"Game over! The word was: {game.get_word_to_guess()}")
            button.config(text="New Game", command=new_game)
        else:
            message_label.config(text=f"Letters Guessed: {game.get_letters_guessed()}")
        hidden_word_label.config(text=game.get_display())

    draw_gallows(game)


game = hangman.Hangman()

hidden_word_label = tk.Label(frame, text=game.get_display())
hidden_word_label.pack()

# TextBox Creation
inputtxt = tk.Text(frame, height=1, width=20)

inputtxt.pack()

# Button Creation
button = tk.Button(frame, text="Guess a letter", command=handle_click)
button.pack()

# Label Creation
message_label = tk.Label(frame, text="")
message_label.pack()

canvas = tk.Canvas()
canvas.pack()

draw_gallows(game)

frame.mainloop()