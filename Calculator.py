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
        return "Cannot divide by zero!"

print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Perform All Operations")
print("6. Exit Program")

while True:
    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Exiting the program.")
        break

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "+", num2, "=", add(num1, num2))
            print(num1, "-", num2, "=", subtract(num1, num2))
            print(num1, "*", num2, "=", multiply(num1, num2))
            print(num1, "/", num2, "=", divide(num1, num2))
        print("------------------------------------")
    else:
        print("Invalid input. Please enter a valid choice.")
