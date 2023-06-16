#!/usr/bin/python3 

def add_numbers():
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

    total = sum(numbers)
    print("The sum of the numbers is:", total)

# Call the add_numbers function
My_homework_tonight=add_numbers()

#Print the result on the screen

print(My_homework_tonight)
