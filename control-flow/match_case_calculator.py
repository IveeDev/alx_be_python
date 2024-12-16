num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Enter type of arithmetic operations
arith_operations = input("Choose the operation (+, -, *, /): ")

match arith_operations:
    case "+":
        print(f"The result is {num1 + num2}.")
    case "-":
        print(f"The result is {num1 - num2}.")
    case "*":
        print(f"The result is {num1 * num2}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {num1 / num2}.")
    case _:
        print("Invalid operation")
