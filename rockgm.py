import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 1 and computer_choice == 3) or
        (user_choice == 2 and computer_choice == 1) or
        (user_choice == 3 and computer_choice == 2)
    ):
        return "You win!"
    else:
        return "You lose!"

def display_choices(choice):
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    return choices.get(choice, 'Invalid choice')

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0
    valid_choices = [1, 2, 3]

    print("Welcome to Rock-Paper-Scissors Game!")
    print("Enter 1 for Rock, 2 for Paper, 3 for Scissors")

    while True:
        print("\nScore - You: {} | Computer: {}".format(user_score, computer_score))

        # User input
        try:
            user_choice = int(input("Enter your choice (or '0' to quit): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Check if the user wants to quit
        if user_choice == 0:
            print("Thanks for playing! Final Score - You: {} | Computer: {}".format(user_score, computer_score))
            break

        # Check if the user's input is valid
        if user_choice not in valid_choices:
            print("Invalid choice. Please enter 1 for Rock, 2 for Paper, or 3 for Scissors.")
            continue

        # Computer's random choice
        computer_choice = random.choice(valid_choices)

        # Display choices
        print("Your choice: {}".format(display_choices(user_choice)))
        print("Computer's choice: {}".format(display_choices(computer_choice)))

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

if __name__ == "__main__":
    rock_paper_scissors_game()
