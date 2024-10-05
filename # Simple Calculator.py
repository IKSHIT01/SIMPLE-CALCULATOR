# Simple Calculator

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation selected."

# Displaying the menu
def show_menu():
    print("\nCalculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

# Main program
while True:
    try:
        # Asking the user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Showing the operation menu
        show_menu()
        
        # Asking for the user's choice of operation
        operation = input("Choose an operation (1/2/3/4): ")
        
        # Performing the calculation and displaying the result
        result = calculate(num1, num2, operation)
        print(f"Result: {result}")
        
        # Asking if the user wants to perform another calculation
        continue_calc = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if continue_calc != 'yes':
            print("Exiting the calculator. Goodbye!")
            break
    except ValueError:
        print("Invalid input. Please enter numbers only.")
