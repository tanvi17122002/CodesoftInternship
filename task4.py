import random

def get_user_choice():
    choice = input("Choose Rock, Paper, or Scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        choice = input("Choose Rock, Paper, or Scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYour choice: {user_choice.capitalize()}")
        print(f"My choice: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"\nScore - You: {user_score} | Computer: {computer_score}\n")

        play_again = input("Do you want to play again? (Yes/No): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

if _name_ == "_main_":
    main()