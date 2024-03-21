def accept_users_name():
    while True:
        name = input("Enter your name: ").capitalize()
        if not name.isalpha():
            print("Please user letters.")
            continue
        else:
            return name
