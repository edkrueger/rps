from random import randint

def is_valid(choice):
    
    if choice == None:
        return False

    if choice.lower() in {"r", "p", "s"}:
        return True

    return False

def prompt_choice():
    choice = None

    while not is_valid(choice):
        choice = input("Choose R/P/S!")   
    return choice

def play():
    player_choice = prompt_choice()
    print(f"You chose... {player_choice}")
    ai_choice = ["r", "p", "s"][(randint(0, 2))]
    print(f"Computer chose... {ai_choice}")
    determine_winner(player_choice, ai_choice)

def determine_winner(player_choice, ai_choice):
    player_choice = player_choice.lower()
    if player_choice == ai_choice:
        print("It's a draw!")
    elif (ai_choice == "r" and player_choice == "s") or \
        (ai_choice == "s" and player_choice == "p") or \
        (ai_choice == "p" and player_choice == "r"):
        print("Computer wins!")
    else:
        print("Player wins!")

if __name__ == "__main__":
    play()