while True:
    print("\n=== Simple Calculator ===")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Choose operation: +, -, *, /, or 'quit' to exit")
    operation = input("Operation: ")
    
    if operation == "quit":
        print("Goodbye!")
        break
    elif operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        result = "Invalid operation!"
    
    print("Result:", result)
