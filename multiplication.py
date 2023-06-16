#!/usr/bin/python3 
def multiply_numbers():
    numbers = []
    while True:
        num = input("Enter a number (or 'q' to quit): ")
        if num.lower() == 'q':
            break
        try:
            num = float(num)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")

    total = 1
    for num in numbers:
        total *= num

    print("The multiplication of the numbers is:", total)

#Let us call the function

multiply_numbers()
