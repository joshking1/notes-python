#!/usr/bin/python3 

def subtract_numbers():
    numbers = []
    while True:
        num = input("Enter a number: ")
        try:
            num = float(num)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number.")

        if len(numbers) >= 2: # We are going to enter the numbers until we get at least two numbers. 
            break

    result = numbers[0] - numbers[1]  # Subtract the second number from the first number

    print("The subtraction of the two numbers is:", result)

# Let us call the function

subtract_numbers()
