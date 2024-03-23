def accept_users_name():
    while True:
        name = input("Enter your name: ").capitalize()
        if name.isalpha():
            return name
        else:
            continue
