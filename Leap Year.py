# Defining the function days_in_feb with user_year as the parameter
def days_in_feb(user_year):
    """ Logic: For a year to be considered as a leap year:
      1) The year must be divisible by 4
      2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400"""

    if (user_year % 4) == 0:
        # If the year is a century year
        if (user_year % 100) == 0:
            # It must be evenly divisible by 400
            if (user_year % 400) == 0:
                # Initializing the variable leap as True or False accordingly
                leap = True
            else:
                leap = False

        else:
            leap = True
    else:
        leap = False
    if leap == True:
        # Printing the desired output
        print(user_year, "is a leap year.")
    else:
        print(user_year, "is not a leap year.")


# Test Case
if __name__ == '__main__':
    user_year = int(input("Enter the year: "))
    days_in_feb(user_year)
