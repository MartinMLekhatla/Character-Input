def display_turns_100_message(name, age, year_hundred):
    if age < 0 or not isinstance(age, (int, float)):
        return f'Invalid age input. Please enter a valid age.'
    return f'Hello, {name}! You will turn 100 years old in the year {year_hundred} since you are currently {age}.'
