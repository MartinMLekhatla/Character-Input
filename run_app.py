# Assuming the relevant functions are defined in these modules
from src.user_input import accept_user_name, accept_user_age
from src.calculate_year import calculate_year_turns_100
from src.display_message import display_turns_100_message

def run_application():
    # Get user's name
    name = accept_user_name()
    # Get user's age
    age = accept_user_age()
    # Calculate the year the user turns 100
    year_user_turns_100 = calculate_year_turns_100(age)
    # Display the message
    print(display_turns_100_message(name, age, year_user_turns_100))

if __name__ == '__main__':
    run_application()
