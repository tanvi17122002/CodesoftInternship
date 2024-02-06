def calculator():
    # Prompt user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Prompt user for operation choice
    operation = input("Choose an operation (+, -, *, /): ")
    
    # Perform calculation based on user's choice
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        # Check for division by zero
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Error: Invalid operation"
    
    # Display the result
    return f"Result: {result}"

# Call the calculator function
print(calculator())