from datetime import datetime


def accept_users_name():
    while True:
        name = input("Enter your name: ").capitalize()
        if name.isalpha():
            return name
        else:
            continue


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


def display_turns_100_message(name, age, year_hundred):
    if age < 0 or not isinstance(age, (int, float)):
        return f'Invalid age input. Please enter a valid age.'
    return f'Hello, {name}! You will turn 100 years old in the year {year_hundred} since you are currently {age}.'


def run_application():
    name = accept_users_name()
    age = accept_users_age()
    year_user_turns_100 = calculate_year_turns_100(age)
    print(display_turns_100_message(name, age, year_user_turns_100))


if __name__ == '__main__':
    run_application()
