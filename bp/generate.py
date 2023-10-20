def generate_birthdays(N):
    import random
    return [ random.randint(1,365) for i in range(N) ]
