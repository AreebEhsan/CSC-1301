# Prolog
# Author: AREEB EHSAN
# Email: aehsan1@student.gsu.edu
# Section: CS 1301


# Taking input from the user
num = int(input("Enter the 10 digit phone number: "))

# Extracting the required digits by performing three different operations
var1 = num // 10000000
var2 = (num // 10000) % 1000
var3 = num % 10000

# Converting into string datatype
i = str(var1)
j = str(var2)
k = str(var3)

# Printing the output
print("(" + i + ")", j + "-" + k)

"""Test Case : 
Enter the 10 digit phone number: 1234567890
(123) 456-7890

Process finished with exit code 0 """
