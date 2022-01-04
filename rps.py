from random import randint

def validate_choice(choice):
    if not choice.lower() in {"r", "p", "s"}:
        raise ValueError("Must be one of R, P or S!")
        
def prompt_choice():
    
    choice = input("Choose R/P/S!")   
    validate_choice(choice)
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