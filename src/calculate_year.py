from datetime import datetime

def calculate_year_turns_100(age):
    """
    Calculate the year when someone will turn 100 years old based on their current age.

    Parameters:
    age (int): The current age of the person in years.

    Returns:
    int: The year the person will turn 100 years old.
    """
    if not isinstance(age, int):
        raise ValueError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")

    year_hundred = datetime.now().year + (100 - age)
    return year_hundred
