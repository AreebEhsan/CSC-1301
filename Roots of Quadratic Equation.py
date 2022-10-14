import math

print("Enter the coefficients below:")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a == 0:
    raise NotImplementedError
else:
    delta = b * b - 4 * a * c
    if delta > 0:
        root_1 = (-b + math.sqrt(delta)) / (2 * a)
        root_2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Roots are real and unequal")
        print("Root1=", root_1, "Root2=", root_2)
    elif delta == 0:
        root_1 = -b / (2 * a);
        print("Roots are real and equal.")
        print("Root1=", root_1, "Root2=", root_1)
    else:
        print("Roots are complex and imaginary.")
