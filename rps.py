def validate_choice(choice):
    if not choice.lower() in {"r", "p", "s"}:
        raise ValueError("Must be one of R, P or S!")
        
def prompt_choice():
    
    choice = input("Choose R/P/S!")   
    validate_choice(choice)
    return choice

def play():
    choice = prompt_choice()
    print(f"You chose... {choice}")
    
if __name__ == "__main__":
    play()