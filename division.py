#!/usr/bin/python3 
def divide_numbers():
    numbers = []
    while True: # Continue until exactly two numbers are entered
        num = input("Enter a number: ")
        try:
            num = float(num)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number.")
        if len(numbers) >= 2: 
           break

    total = numbers[0] / numbers[1]  # Divide the first number by the second number

    print("The division of the two numbers is:", total)

# Let us call the function
divide_numbers()

