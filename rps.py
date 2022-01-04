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
    choice = prompt_choice()
    print(f"You chose... {choice}")
    
if __name__ == "__main__":
    play()