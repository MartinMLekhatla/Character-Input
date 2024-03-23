def accept_users_age():
    age_str = input("Enter your age: ")
    try:
        age = int(age_str)
        return age
    except ValueError:
        return None
