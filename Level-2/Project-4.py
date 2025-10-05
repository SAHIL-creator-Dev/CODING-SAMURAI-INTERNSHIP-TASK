#  Number Guessing Game with GUI 
import tkinter as tk
import random

def check_guess():
    try:
        user_guess = int(entry_guess.get())
    except ValueError:
        label_result.config(text="⚠️ Please enter a valid number!", fg="red")
        return

    global attempts
    attempts += 1
    difference = abs(number_to_guess - user_guess)

    if user_guess < number_to_guess:
        if difference <= 5:
            label_result.config(text=f"🔽 A little low! You’re very close. (Attempt {attempts})", fg="#007BFF")
        else:
            label_result.config(text=f"🔽 Too low! Try a higher number. (Attempt {attempts})", fg="#007BFF")
    elif user_guess > number_to_guess:
        if difference <= 5:
            label_result.config(text=f"🔼 A little high! You’re very close. (Attempt {attempts})", fg="#FF5733")
        else:
            label_result.config(text=f"🔼 Too high! Try a lower number. (Attempt {attempts})", fg="#FF5733")
    else:
        label_result.config(text=f"🎉 Correct! The number was {number_to_guess}.\nYou guessed it in {attempts} tries!", fg="green")
        btn_check.config(state="disabled")
        btn_restart.config(state="normal")

def restart_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    label_result.config(text="Guess a number between 1 and 100!", fg="black")
    entry_guess.delete(0, tk.END)
    btn_check.config(state="normal")
    btn_restart.config(state="disabled")

root = tk.Tk()
root.title("🎯 Number Guessing Game")
root.geometry("430x330")
root.config(bg="#F5F5F5")

label_title = tk.Label(root, text="🎯 Number Guessing Game", font=("Arial", 16, "bold"), bg="#F5F5F5", fg="#333")
label_title.pack(pady=15)

label_instruction = tk.Label(root, text="I'm thinking of a number between 1 and 100", font=("Arial", 12), bg="#F5F5F5")
label_instruction.pack()

entry_guess = tk.Entry(root, font=("Arial", 12), justify="center", width=10)
entry_guess.pack(pady=10)

btn_check = tk.Button(root, text="Check Guess", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=check_guess, width=12)
btn_check.pack(pady=5)

label_result = tk.Label(root, text="Guess a number between 1 and 100!", font=("Arial", 12), bg="#F5F5F5", fg="black", wraplength=400, justify="center")
label_result.pack(pady=15)

btn_restart = tk.Button(root, text="Play Again", font=("Arial", 12, "bold"), bg="#2196F3", fg="white", command=restart_game, state="disabled", width=12)
btn_restart.pack(pady=5)

number_to_guess = random.randint(1, 100)
attempts = 0

root.mainloop()
