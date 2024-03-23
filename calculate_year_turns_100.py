from datetime import datetime


def calculate_year_turns_100(age):
    # Check if the age is not numeric
    if not isinstance(age, (int, float)):
        return None

    # Check if the age is negative
    if age < 0:
        return None
    year_hundred = datetime.now().year + (100 - age)
    return year_hundred
