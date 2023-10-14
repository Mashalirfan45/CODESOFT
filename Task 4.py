import random
import tkinter as tk
from tkinter import messagebox
# Initialize scores for the user and computer
user_score = 0
computer_score = 0
# Function to handle the user's choice
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    # Determine the winner
    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        result_label.config(text="You win!🙌🏆")
        user_score += 1
    else:
        result_label.config(text="Computer wins!🙌🏆")
        computer_score += 1

    # Update the scores
    user_score_label.config(text=f"Your score: {user_score}")
    computer_score_label.config(text=f"Computer's score: {computer_score}")

    # Ask if the user wants to play again
    answer = messagebox.askyesno("Play Again?", "Do you want to play again?")
    if answer:
        result_label.config(text="")
    else:
        show_final_result()

# Function to display the final result
def show_final_result():
    result_label.config(text=f"Final Score:\n")
    if user_score > computer_score:
        result_label.config(text=result_label.cget("text") + "\nYou Win!🎉\n" "Thanks for playing")
    elif user_score < computer_score:
        result_label.config(text=result_label.cget("text") + "\nComputer Wins!🎉")
    else:
        result_label.config(text=result_label.cget("text") + "\nIt's a Tie!🙁")
# Create a Tkinter window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")
# Create labels and buttons
window.geometry("400x200")
instruction_label = tk.Label(window, text="Choose rock, paper, or scissors:")
instruction_label.pack()

rock_button = tk.Button(window, text="Rock", command=lambda: play('rock'))
paper_button = tk.Button(window, text="Paper", command=lambda: play('paper'))
scissors_button = tk.Button(window, text="Scissors", command=lambda: play('scissors'))
rock_button.pack()
paper_button.pack()
scissors_button.pack()

result_label = tk.Label(window, text="", font=("times new roman", 16))
result_label.pack()

user_score_label = tk.Label(window, text="Your score: 0", font=("times new roman", 12))
user_score_label.pack()

computer_score_label = tk.Label(window, text="Computer's score: 0", font=("times new roman", 12))
computer_score_label.pack()
# Start the Tkinter main loop
window.mainloop()
