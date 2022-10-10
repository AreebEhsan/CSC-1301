# Highway number input by user
highway_num = str(input("Enter interstate highway number: "))

# Adding "I-" before the highway number (appropriate format of US interstate highways)
interstate_highway = "I-" + highway_num

# Extracting the last two digits for performing further operations
highway_number = int(interstate_highway[2:])

# Determining the type and validity of interstate highways and printing the outputs
# Use of nested if-else statements


# Determination of auxiliary highways
if len(str(highway_number)) == 3 and highway_number % 100 != 0:

    # Determination of directions
    if highway_number % 2 == 0:
        print(interstate_highway, "is auxiliary, serving I-" + str(highway_number % 100), "going east/west.")
    else:
        print(interstate_highway, "is auxiliary, serving I-" + str(highway_number % 100), "going north/south")

# Determination of primary highways
elif len(str(highway_number)) == 2:
    if highway_number % 2 == 0:

        # Determination of directions
        print(interstate_highway, "is primary, going east/west.")
    else:
        print(interstate_highway, "is primary, going north/south.")

# Validity
elif highway_number == 00:
    print(highway_number, "is not a valid interstate highway number.")

else:
    print(highway_number, "is not a valid interstate highway number.")
