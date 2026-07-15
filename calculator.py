import math

# Functions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b

def square(a):
    return a * a

def square_root(a):
    if a < 0:
        return "Error! Square root of a negative number is not possible."
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error! Factorial of a negative number is not possible."
    return math.factorial(a)


# Main Program
while True:
    print("\n*** CALCULATOR ***")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square")
    print("8. Square Root")
    print("9. Factorial")
    print("10. Exit")

    choice = int(input("Enter your choice (1-10): "))

    if choice == 10:
        print("Thank you for using the calculator!")
        break

    elif choice in [1, 2, 3, 4, 5, 6]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", addition(num1, num2))
        elif choice == 2:
            print("Result =", subtraction(num1, num2))
        elif choice == 3:
            print("Result =", multiplication(num1, num2))
        elif choice == 4:
            print("Result =", division(num1, num2))
        elif choice == 5:
            print("Result =", modulus(num1, num2))
        elif choice == 6:
            print("Result =", power(num1, num2))

    elif choice == 7:
        num = float(input("Enter a number: "))
        print("Result =", square(num))

    elif choice == 8:
        num = float(input("Enter a number: "))
        print("Result =", square_root(num))

    elif choice == 9:
        num = int(input("Enter a non-negative integer: "))
        print("Result =", factorial(num))

    else:
        print("Invalid choice! Please enter a number between 1 and 10.")