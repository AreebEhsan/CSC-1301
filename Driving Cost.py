"""Define that function in a program whose inputs are the car's miles per gallon
and the price of gas in dollars per gallon (both float). Output the gas cost for
10 miles, 50 miles, and 400 miles, by calling your driving_cost() function three
times"""

# Defining the function driving_cost with three parameters
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    # Logic:_ total driving cost = miles driven * (cost per gallo`n/miles per gallon)
    num_gallons = (miles_driven / miles_per_gallon)
    cost = num_gallons * dollars_per_gallon

    # Returning the required result
    return cost


# Format:-
if __name__ == '__main__':
    # Taking input from the user
    miles_per_gallon = float(input("Enter the miles per gallon: "))
    dollars_per_gallon = float(input("Enter the dollars per gallon: "))

    # Applying the function 3 times for required miles
    total_cost1 = driving_cost(miles_per_gallon, dollars_per_gallon,10)  # Miles driven value already provided
    total_cost2 = driving_cost(miles_per_gallon, dollars_per_gallon,50)
    total_cost3 = driving_cost(miles_per_gallon,dollars_per_gallon,400)
    # Printing the output
print(f'{total_cost1:.2f}')
print(f'{total_cost2:.2f}')
print(f'{total_cost3:.2f}')


