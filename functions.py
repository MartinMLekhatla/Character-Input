from datetime import datetime


def accept_users_name():
    name = input("Enter your name: ").capitalize()
    return name


def accept_users_age():
    age_str = input("Enter your age: ")
    try:
        age = int(age_str)
        return age
    except ValueError:
        return None


def calculate_year_turns_100(age):
    # Check if the age is not numeric
    if not isinstance(age, (int, float)):
        return None

    # Check if the age is negative
    if age < 0:
        return None
    year_hundred = datetime.now().year + (100 - age)
    return year_hundred

