def display_turns_100_message(name, age, year_hundred):
    """
    Construct a message informing the user of the year they will turn 100 years old.

    Parameters:
    name (str): The name of the person.
    age (int): The current age of the person. Assumes age has been validated as non-negative integer.
    year_hundred (int): The future year when the person will turn 100.

    Returns:
    str: A greeting message that includes the year the person will turn 100.
    """
    return f'Hello, {name}! You will turn 100 years old in the year {year_hundred}, since you are currently {age}.'
