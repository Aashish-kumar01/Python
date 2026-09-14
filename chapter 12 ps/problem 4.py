a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2st number: "))

try:
    print(f"The division of the digits {a} and {b} is {a/b}")
except ZeroDivisionError as e:
    print("Infinite")