"""
Birthday Problem implementation package
"""

def main(N=23, X=100):
    """
    Main function of BP

    - N
    -X
    """
    cnt = 0
    for i in range(X):

        ## generate 'N' birthdays
        birthdays = generate_birthdays(N)

        ## Check for equal birthdays, increment 'cnt' if so
        cnt += check_birthdays(birthdays)

    print(f"Probability of same birthdays in a group of {N} people:", cnt/X)
