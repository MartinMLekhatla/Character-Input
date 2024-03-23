import accept_user_name
import accept_users_age
import calculate_year_turns_100
import display_turns_100_message


def run_application():
    name = accept_user_name.accept_users_name()
    age = accept_users_age.accept_users_age()
    year_user_turns_100 = calculate_year_turns_100.calculate_year_turns_100(age)
    print(display_turns_100_message.display_turns_100_message(name, age, year_user_turns_100))


if __name__ == '__main__':
    run_application()
