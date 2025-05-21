def add(x, y):
    """Add two numbers."""
    return x + y
def subtract(x, y):
    """Subtract two numbers."""
    return x - y
def multiply(x, y):
    """Multiply two numbers."""
    return x * y
def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    print("Welcome to the Simple Calculator!")
    print("--------------------------------")

    # Initialise a flag to control the calculator loop
    continue_calculating = True

    while continue_calculating:
        print("/nAvailable operations:")
        print("1. Addition(+)")
        print("2. Subtraction(-)")
        print("3. Multiplication(*)")
        print("4. Division(/)")

        # Get user input for operation choice and numbers
        try:
            choice = input("/nEnter operation choice (1-4): ")

            # Check if the choice is valid
            if not choice.isdigit():
                raise ValueError("Invalid input. Please enter a number between 1 and 4.")
            choice = choice.strip()
            # Check if the choice is within the valid range
            if choice not in ['1', '2', '3', '4']:
                raise ValueError("Invalid choice. Please select a valid operation. Enter a number between 1 and 4.")
                continue

            # Get user input for numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))


            # Perform the selected operation
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    operation = "/"
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
            
            # Display the result
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        
        except ValueError as e:
            if "divide by zero" in str(e):
                print("Error: Cannot divide by zero.")
            else:
                print("Error: Please enter valid numbers!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        # Ask if the user wants to perform another calculation
        while True:
            continue_choice = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
            if continue_choice in ['yes', 'y']:
                break
            elif continue_choice in ['no', 'n']:
                continue_calculating = False
                print("Thank you for using the calculator. Goodbye!")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    
    print("\nThank you for using the Simple Calculator. Goodbye!")

if __name__ == "__main__":
    main()
# calculator.py