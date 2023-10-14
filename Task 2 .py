import math
import os
class Calculator:
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return("\033[1;31mError!!: Division by zero is not defined. \033[0m")

    def find_percentage(x, percentage):
        return (percentage / 100) * x

    def square_root(x):
        if x >= 0:
            return math.sqrt(x)
        else:
            print("\033[1;31mMath Error!!!: \033[0mPlease enter positive numbers")# Red text for errors
    def square(x):
        return x * x
def main():
    print('\n')
    print(f"{' ' * 6}........||CALCULATOR||.....{'' * 3}")
    print(f"......||THE NO OF OPERATIONS YOU CAN PERFORM||.......")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Find Percentage")
    print("6. Square Root")
    print("7. Square")
    print("8. Quit")

    while True:
        operation = input("\nEnter operation which you want to perform: ")
        if operation == '8':
            print("Thank You")
            break
        if operation in ('1', '2', '3', '4', '5', '6', '7'):
            num1 = float(input("Enter first number: "))
            
            if operation != '6' and operation != '7'and operation != '5':
                num2 = float(input("Enter second number: "))

            if operation == '1':
                result = Calculator.add(num1, num2)
                print("ADDITION OF ",num1, "+", num2, "=", result)
            elif operation == '2':
                result = Calculator.subtract(num1, num2)
                print("SUBTRACTION OF ",num1, "-", num2, "=", result)
            elif operation == '3':
                result = Calculator.multiply(num1, num2)
                print("MULTIPLICATION OF ",num1, "*", num2, "=", result)
            elif operation == '4':
                result = Calculator.divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                   print("...DIVISION OF ",num1, "/", num2, "=", result)
            elif operation == '5':
                percentage = float(input("Enter the percentage to find (e.g., 10 for 10%): "))
                result = Calculator.find_percentage(num1, percentage)
                print(f"{percentage}% of {num1} is {result}")
            elif operation == '6':
                result = Calculator.square_root(num1)
                print(f"Square root of {num1} = {result}")
            elif operation == '7':
                result = Calculator.square(num1)
                print(f"Square of {num1} = {result}")
        else:
            print("Invalid input. Please enter a valid operation from the options I've provided.")

if __name__ == "__main__":
    main()
