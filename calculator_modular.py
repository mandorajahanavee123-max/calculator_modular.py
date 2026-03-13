# Internship Task 5: Functions & Modular Programming

# 1. Define functions for add, subtract, multiply, divide

def add(a, b=0):
    """Return the sum of a and b. Default b=0."""
    return a + b

def subtract(a, b=0):
    """Return the difference of a and b. Default b=0."""
    return a - b

def multiply(a, b=1):
    """Return the product of a and b. Default b=1."""
    return a * b

def divide(a, b=1):
    """Return the division of a by b. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# 2. Function to handle user choice
def calculator():
    """Main calculator function to perform operations based on user input."""
    print("Welcome to the Modular Calculator!\n")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid choice. Please select 1-4.")

# 3. Test functions independently
if __name__ == "__main__":
    # Independent function tests
    print("Testing functions individually:")
    print("Add 5 + 3:", add(5, 3))
    print("Subtract 10 - 4:", subtract(10, 4))
    print("Multiply 6 * 7:", multiply(6, 7))
    print("Divide 8 / 2:", divide(8, 2))
    print("Divide 5 / 0:", divide(5, 0))
    print("\nLaunching interactive calculator...\n")
    
    # Run the calculator
    calculator()