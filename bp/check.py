def check_birthdays(birthdays):
    unique_birthdays = set(birthdays)
    return len(birthdays) != len(unique_birthdays)
