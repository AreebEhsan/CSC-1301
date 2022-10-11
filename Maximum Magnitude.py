# Prolog
# Author: AREEB EHSAN
# Email: aehsan1@student.gsu.edu
# Section: CS 1301 Lab 22

# Defining the function
def max_magnitude(user_val1, user_val2, user_val3):
    # Logic:- If the value equals the maximum absolute value then return that else return the negative the maximum absolute value.

    if user_val1 == max(abs(user_val1), abs(user_val2), abs(user_val3)):
        return user_val1
    elif user_val2 == max(abs(user_val1), abs(user_val2), abs(user_val3)):
        return user_val2
    elif user_val3 == max(abs(user_val1), abs(user_val2), abs(user_val3)):
        return user_val3
    else:
        return -max(abs(user_val1), abs(user_val2), abs(user_val3))


# Format:-
if __name__ == '__main__':
    # Taking inputs
    user_val1 = int(input("Enter first number: "))
    user_val2 = int(input("Enter second number: "))
    user_val3 = int(input("Enter third number: "))

    # Printing the output
    print(max_magnitude(user_val1, user_val2, user_val3))
