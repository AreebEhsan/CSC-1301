# Taking list as input from the user
lst = []

n = int(input("Enter number of elements: "))

for i in range(0, n):

    ele = int(input("Enter elements: "))

    lst.append(ele)

print("List to be reversed: ", lst)

print("Reversed list is: ")

print(lst[::-1])
