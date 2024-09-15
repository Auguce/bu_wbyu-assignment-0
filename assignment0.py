def add_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print("This program will print the result of adding two numbers.")
    
    # Prompt the user for the first number
    first_number = float(input("Please enter the first number: "))
    
    # Prompt the user for the second number
    second_number = float(input("Please enter the second number: "))
    
    # Calculate the sum
    result = add_two_numbers(first_number, second_number)
    
    # Print the result in the form of an equation
    print(f"The result of {first_number} + {second_number} is {result}.")

