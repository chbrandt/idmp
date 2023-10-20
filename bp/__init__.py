def generate_birthdays(N):
    import random
    return [ random.randint(1,365) for i in range(N) ]

def check_birthdays(birthdays):
    unique_birthdays = set(birthdays)
    return len(birthdays) != len(unique_birthdays)

def main(N=23, X=100):
    cnt = 0
    for i in range(X):

        ## generate 'N' birthdays
        birthdays = generate_birthdays(N)

        ## Check for equal birthdays, increment 'cnt' if so
        cnt += check_birthdays(birthdays)

    print(f"Probability of same birthdays in a group of {N} people:", cnt/X)
