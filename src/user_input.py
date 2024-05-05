def accept_user_age():
    """
    Prompt the user to enter their age until they provide a valid non-negative integer.

    Returns:
    int: The age entered by the user.
    """
    while True:
        age_input = input("Please enter your age: ")
        if age_input.isdigit() and int(age_input) >= 0:
            return int(age_input)
        else:
            print("Invalid input. Please enter a non-negative integer for age.")

def accept_user_name():
    """
    Prompt the user to enter their name until they provide a valid name that does not include numbers and is not empty.

    Returns:
    str: The name entered by the user, with the first letter capitalized and extraneous spaces removed.
    """
    while True:
        name = input("Please enter your name: ").capitalize()
        if name.strip() == "":
            print("Input cannot be empty. Please enter a valid name.")
        elif any(char.isdigit() for char in name):
            print("Invalid input. Names should not contain numbers.")
        else:
            return name
